#! -*-conding=: UTF-8 -*-
# @Time    : 2024/05/06 17:18
# @Author  : 海哥python
# @Software: PyCharm

import re
import json
import sys

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


def get_response_data(url, headers, cookies):
    response = session.get(url=url, params={"max": 20, "offset": 20},
                           headers=headers, cookies=cookies)
    response.encoding = "utf-8"
    logger.success(response.text)


def get_second_cookies(cookies, go_params):
    __jsl_clearance_s = execjs.compile(open("final.js", "r", encoding="utf-8").read()).call("go", go_params)
    logger.info(go_params)
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
