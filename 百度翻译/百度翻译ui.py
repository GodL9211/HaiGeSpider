#! -*-conding=: UTF-8 -*-
# 2024/4/29 11:12

from urllib import request
from http import cookiejar
import re
import time
import tkinter as tk
from os import path

import requests
import execjs
from loguru import logger
import urllib3

# 禁用 SSL 验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 解决打包后图片找不到的问题
def _abspath(file_path):
    return path.abspath(path.join(path.dirname(__file__), file_path))


class BaiduTranslateUI:
    def __init__(self, root):
        self.root = root
        self.root.title("bd翻译软件-公众号：海哥python")

        # 创建界面元素
        self.label = tk.Label(root, text="请输入你想要翻译的词语或句子：")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.translate_button = tk.Button(root, text="翻译", command=self.translate)
        self.translate_button.pack()

        self.translation_label = tk.Label(root, text="")
        self.translation_label.pack()

        self.quit_button = tk.Button(root, text="退出", command=root.quit)
        self.quit_button.pack()

        # 初始化翻译类
        self.tra = BaiduTranslate()

    def translate(self):
        input_key = self.entry.get().strip()
        if not input_key:
            self.translation_label.config(text="请输入有效的词语或句子。")
            return

        try:
            translation = self.tra.translate(input_key)
            self.translation_label.config(text=f"翻译结果: {translation}")
        except Exception as e:
            logger.exception(f"发生异常: {e}")
            self.translation_label.config(text=f"翻译失败，请检查网络连接或稍后再试: {e}")


class BaiduTranslate:
    def __init__(self):
        self.session = requests.Session()
        self.index_url = "https://fanyi.baidu.com/"
        self.baidu_url = 'http://www.baidu.com'
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept": "*/*",
            # 'Cookie': 'BAIDUID=2075799560CB805468E46C062291C3CA:FG=1; PSTM=1710310886; BIDUPSID=B15467B23371BD127587BB726566C72B; BDUSS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; BDUSS_BFESS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; newlogin=1; H_PS_PSSID=40304_40080_40463; H_WISE_SIDS=40304_40080_40463; BAIDUID_BFESS=2075799560CB805468E46C062291C3CA:FG=1; ZFY=R542yFk7iD7:B0KVN:AELgNejr4Bl5IeQAioFd9VbCgkY:C; H_WISE_SIDS_BFESS=40304_40080_40463; smallFlowVersion=old; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[r5ISJbddYbD]=3yOp2bF5zzbmhF1Tv38mvqV; BA_HECTOR=8ka58h2g21ag242ka185840g601h1q1j2rc2n1s; PSINO=6; delPer=0; BCLID=6565329525091269733; BCLID_BFESS=6565329525091269733; BDSFRCVID=xnuOJeC62w-31-ctaErjUmHOVg3SOxnTH6aoyisApyjRGOU0mrB4EG0PaU8g0KubrqyqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=xnuOJeC62w-31-ctaErjUmHOVg3SOxnTH6aoyisApyjRGOU0mrB4EG0PaU8g0KubrqyqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJk8oDPbJK03fP36q4jqMJtJ5eT22jn42Jb9aJ5y-J7nhnnTDPbM-fLXDnoLBURp523ion3vQpbZql5EbJjb2jkbWxTEJp5lLIn9Kl0MLP-WoJklQfrD3h3QXfnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRD5uhDjObDaRK5b30bD5JX6rD5RT5j-Kk-PI32-C0XP6-35KHb-Deo66JbnjpqRcahf7c34by0PnO2q37JD6yXRTb04JBjxojXp_2hJDYj-oxJpOKQRbMopvaKtoaJtjvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIE3-oJqCKMbDL43j; H_BDCLCKID_SF_BFESS=tJk8oDPbJK03fP36q4jqMJtJ5eT22jn42Jb9aJ5y-J7nhnnTDPbM-fLXDnoLBURp523ion3vQpbZql5EbJjb2jkbWxTEJp5lLIn9Kl0MLP-WoJklQfrD3h3QXfnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRD5uhDjObDaRK5b30bD5JX6rD5RT5j-Kk-PI32-C0XP6-35KHb-Deo66JbnjpqRcahf7c34by0PnO2q37JD6yXRTb04JBjxojXp_2hJDYj-oxJpOKQRbMopvaKtoaJtjvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIE3-oJqCKMbDL43j; RT="z=1&dm=baidu.com&si=8b8aca4f-f75c-474e-94aa-7edaa05d914f&ss=lvizc8dk&sl=3&tt=51h&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=o2bb&ul=o3jn&hd=o3nm"; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.1_OGY1YmU0NDFmMmExZjgxZjc1YzYxYmYxNDcxN2E1YWUxMTQ5YzMyYTA4ZGI0MzU2ZDRkY2MzNTkwNGQ3MjBiNjc5ZDAyMGQ3ZTYxYTg5ZGFhNDQyYzliNTU4MmU5ZjM1YmRhNDQ5NDhlZGJiYjc0NzkwZTdlYzI1MjM0ZTg0ZGQ5MDVlMWU1ZjNkZGU3NzgzZTc0OTA4ZjRlNzRjY2Q5YzhiMjlmYjVhYTMxNDMzMDViM2E2NmVlZWE3YTdjZTUx',
            'Connection': 'keep-alive',
            # 'Pragma': 'no-cache',
            'Referer': 'https://fanyi.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.gtk = None
        self.js_path = _abspath("./百度翻译.js")
        self.data = {
            'from': 'zh',
            'to': 'en',
            'query': "",
            'simple_means_flag': '3',
            'sign': "",
            'token': '724b81baa4603c1cdd08df6a5ba0e35f',
            'domain': 'common',
            'ts': str(int(time.time() * 1000))
        }
        self.cookies = ""
        self.re_generate_cookie(url=self.baidu_url)  # 获取百度cookie信息

        self.headers["Cookie"] = self.cookies + "smallFlowVersion=old;"
        print(self.headers)

    def re_generate_cookie(self, url,):
        # 创建一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        # 创建一个HTTPCookieProcessor对象来处理cookie
        handler = request.HTTPCookieProcessor(cookie)
        # 创建一个opener，将处理器添加进去
        opener = request.build_opener(handler)
        # 打开网页
        with opener.open(url) as response:
            for item in cookie:
                self.cookies += f"{item.name}={item.value};"

    def get_sign(self, input_key):
        with open(self.js_path, "r", encoding="utf-8") as f:
            sign_js = f.read()
        sign = execjs.compile(sign_js).call("b", input_key, self.gtk)
        return sign

    def key_parameter(self):
        r = self.session.get(self.index_url, headers=self.headers, verify=False)
        self.cookies = r.cookies.get_dict()
        response = r.text
        # 获取页面中的token/gtk
        self.gtk = re.findall('window.gtk = "(.*?)";', response)[0]
        self.data["token"] = re.findall("token: '(.*?)',", response)[0]

    def translate(self, input_key):
        self.key_parameter()
        self.data["query"] = input_key
        # 使用execjs
        self.data["sign"] = self.get_sign(input_key)
        self.data["ts"] = str(int(time.time() * 1000))
        print(self.data)
        response = self.session.post(url=self.url, headers=self.headers, data=self.data, verify=False, cookies=self.cookies)
        # print(response.status_code)
        response.raise_for_status()  # Raise exception for HTTP errors
        translation_data = response.json()

        translation = translation_data['trans_result']['data'][0]['dst']
        return translation


if __name__ == '__main__':
    root = tk.Tk()
    app = BaiduTranslateUI(root)
    root.mainloop()
