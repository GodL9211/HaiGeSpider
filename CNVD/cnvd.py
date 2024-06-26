#! -*-conding=: UTF-8 -*-
# @Author  : 海哥python
# @Software: PyCharm

import hashlib
import re
import json
import execjs
import requests
from loguru import logger
from fake_useragent import UserAgent

session = requests.session()
ua = UserAgent()


def get_first_cookie(url: str, headers) -> dict:
    cookies = {}
    response = session.get(url, headers=headers)
    cookies.update(response.cookies)
    aa_encode_text = re.search('document.cookie=(.*?);location', response.text).group(1)
    __jsl_clearance_s = execjs.eval(aa_encode_text).split(";")[0]
    cookies["__jsl_clearance_s"] = __jsl_clearance_s.split("=")[1]
    logger.info(f"get_first_cookie: {cookies}")
    return cookies


def get_second_cookie_go_params(url, headers: dict, cookies: dict):
    response = session.get(url, headers=headers, cookies=cookies)
    go_params = re.findall(r';go\((.*?)\)</script>', response.text)[0]
    return json.loads(go_params)


def get_final_jsl_clearance(data: dict):
    chars = len(data['chars'])
    for i in range(chars):
        for j in range(chars):
            clearance = data['bts'][0] + data['chars'][i] + data['chars'][j] + data['bts'][1]
            encrypt = None
            if data['ha'] == 'md5':
                encrypt = hashlib.md5()
            elif data['ha'] == 'sha1':
                encrypt = hashlib.sha1()
            elif data['ha'] == 'sha256':
                encrypt = hashlib.sha256()
            encrypt.update(clearance.encode())
            result = encrypt.hexdigest()
            if result == data['ct']:
                return clearance


def get_response_data(url, headers, cookies):
    response = session.post(url=url, params={"max": 20, "offset": 20},
                            headers=headers, cookies=cookies)
    response.encoding = "utf-8"
    logger.success(response.text)


def get_second_cookies(cookies, go_params):
    # 方法一：原始js, 这里只有sha1的，所以md5和sha256时会拿不到数据，请按照教程自己分析
    __jsl_clearance_s = execjs.compile(open("final.js", "r", encoding="utf-8").read()).call("go", go_params)
    logger.info(go_params)
    # 方法二： js改写
    # __jsl_clearance_s = execjs.compile(open("__jsl_clearance_s.js", "r", encoding="utf-8").read()).call(
    # "get__jsl_clearance_s", go_params)

    # 方法三：python改写
    # __jsl_clearance_s = get_final_jsl_clearance(go_params)  # 通过python脚本获取到jsl_clearance_s

    cookies["__jsl_clearance_s"] = __jsl_clearance_s
    logger.debug(f"cookies: {cookies}")

    return cookies


def main():
    url = 'https://www.cnvd.org.cn/flaw/typelist?typeId=27'
    headers = {
        'User-Agent': ua.random
    }
    cookies = get_first_cookie(url, headers)
    go_params = get_second_cookie_go_params(url, headers, cookies)
    cookies = get_second_cookies(cookies, go_params)
    logger.info(go_params)
    get_response_data(url, headers, cookies)


if __name__ == '__main__':
    main()
