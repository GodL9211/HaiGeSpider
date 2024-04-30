# ！ /usr/bin/nev python
# -*-coding:utf8-*-
import re
import time
import tkinter

import js2py
import requests
import execjs
from loguru import logger
import urllib3

# 禁用 SSL 验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class BaiduTranslate:
    def __init__(self):
        self.headers = {
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'Cookie': 'BAIDUID=2075799560CB805468E46C062291C3CA:FG=1; PSTM=1710310886; BIDUPSID=B15467B23371BD127587BB726566C72B; BDUSS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; BDUSS_BFESS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; newlogin=1; H_PS_PSSID=40304_40080_40463; H_WISE_SIDS=40304_40080_40463; BAIDUID_BFESS=2075799560CB805468E46C062291C3CA:FG=1; ZFY=R542yFk7iD7:B0KVN:AELgNejr4Bl5IeQAioFd9VbCgkY:C; H_WISE_SIDS_BFESS=40304_40080_40463; smallFlowVersion=old; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[r5ISJbddYbD]=3yOp2bF5zzbmhF1Tv38mvqV; BA_HECTOR=8ka58h2g21ag242ka185840g601h1q1j2rc2n1s; PSINO=6; delPer=0; BCLID=6565329525091269733; BCLID_BFESS=6565329525091269733; BDSFRCVID=xnuOJeC62w-31-ctaErjUmHOVg3SOxnTH6aoyisApyjRGOU0mrB4EG0PaU8g0KubrqyqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=xnuOJeC62w-31-ctaErjUmHOVg3SOxnTH6aoyisApyjRGOU0mrB4EG0PaU8g0KubrqyqogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJk8oDPbJK03fP36q4jqMJtJ5eT22jn42Jb9aJ5y-J7nhnnTDPbM-fLXDnoLBURp523ion3vQpbZql5EbJjb2jkbWxTEJp5lLIn9Kl0MLP-WoJklQfrD3h3QXfnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRD5uhDjObDaRK5b30bD5JX6rD5RT5j-Kk-PI32-C0XP6-35KHb-Deo66JbnjpqRcahf7c34by0PnO2q37JD6yXRTb04JBjxojXp_2hJDYj-oxJpOKQRbMopvaKtoaJtjvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIE3-oJqCKMbDL43j; H_BDCLCKID_SF_BFESS=tJk8oDPbJK03fP36q4jqMJtJ5eT22jn42Jb9aJ5y-J7nhnnTDPbM-fLXDnoLBURp523ion3vQpbZql5EbJjb2jkbWxTEJp5lLIn9Kl0MLP-WoJklQfrD3h3QXfnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRD5uhDjObDaRK5b30bD5JX6rD5RT5j-Kk-PI32-C0XP6-35KHb-Deo66JbnjpqRcahf7c34by0PnO2q37JD6yXRTb04JBjxojXp_2hJDYj-oxJpOKQRbMopvaKtoaJtjvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIE3-oJqCKMbDL43j; RT="z=1&dm=baidu.com&si=8b8aca4f-f75c-474e-94aa-7edaa05d914f&ss=lvizc8dk&sl=3&tt=51h&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=o2bb&ul=o3jn&hd=o3nm"; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ab_sr=1.0.1_OGY1YmU0NDFmMmExZjgxZjc1YzYxYmYxNDcxN2E1YWUxMTQ5YzMyYTA4ZGI0MzU2ZDRkY2MzNTkwNGQ3MjBiNjc5ZDAyMGQ3ZTYxYTg5ZGFhNDQyYzliNTU4MmU5ZjM1YmRhNDQ5NDhlZGJiYjc0NzkwZTdlYzI1MjM0ZTg0ZGQ5MDVlMWU1ZjNkZGU3NzgzZTc0OTA4ZjRlNzRjY2Q5YzhiMjlmYjVhYTMxNDMzMDViM2E2NmVlZWE3YTdjZTUx',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://fanyi.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
        self.index_url = "https://fanyi.baidu.com/"
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
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
        self.gtk = None
        self.js_path = "./百度翻译.js"

    def get_sign(self, input_key):
        with open(self.js_path, "r", encoding="utf-8") as f:
            sign_js = f.read()
        sign = execjs.compile(sign_js).call("b", input_key, self.gtk)
        return sign

    def generate_sign(self, input_key):
        """生成sign"""
        # 1. 准备js编译环境
        context = js2py.EvalJs()
        with open(self.js_path, "r", encoding='utf8') as f:
            js_data = f.read()
            print(js_data)
            js_data = js_data.replace('320305.131321201', self.gtk)
            context.execute(js_data)
        sign = context.b(input_key, self.gtk)
        return sign

    def key_parameter(self):
        response = self.session.get(self.index_url, headers=self.headers, verify=False).text
        # 获取页面中的token/gtk
        self.data["token"] = re.findall("token: '(.*?)',", response)[0]
        self.gtk = re.findall('window.gtk = "(.*?)";', response)[0]

    def translate(self):
        self.key_parameter()
        while True:
            try:
                input_key = input("请输入你想要翻译的词语或句子：").strip()
                if not input_key:
                    print("请输入有效的词语或句子。")
                    continue
                self.data["query"] = input_key
                # 使用execjs
                self.data["sign"] = self.get_sign(input_key)
                # 或使用js2py
                # self.data["sign"] = self.generate_sign(input_key)
                self.data["ts"] = str(int(time.time() * 1000))
                response = self.session.post(url=self.url, headers=self.headers, data=self.data)
                print(response.status_code)
                response.raise_for_status()  # Raise exception for HTTP errors
                translation_data = response.json()
                translation = translation_data['trans_result']['data'][0]['dst']
                print("翻译结果:", translation)
            except requests.RequestException as e:
                logger.exception(f"请求错误: {e}")
            except (KeyError, IndexError) as e:
                logger.exception(f"翻译结果解析错误或无法获得翻译结果:{e}")
            except Exception as e:
                logger.exception(f"发生异常: {e}")
            finally:
                choice = input("是否继续翻译？(输入 n 退出，其他任意键继续): ")
                if choice.lower() == 'n':
                    break

    def main(self):
        self.translate()


if __name__ == '__main__':
    tra = BaiduTranslate()
    tra.main()
