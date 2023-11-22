#! -*-conding=: UTF-8 -*-
# 2023/11/15 16:39

import base64
import requests
import ddddocr
import execjs
import time
import loguru


class YouZanSliderCaptcha(object):
    """
    target: aHR0cHM6Ly9wYXNzcG9ydC55b3V6YW4uY29tL2xvZ2luL3Bhc3N3b3Jk
    """
    def __init__(self):
        self.base_url = base64.b64decode(b'aHR0cHM6Ly9wYXNzcG9ydC55b3V6YW4uY29tL2FwaS9jYXB0Y2hh').decode()
        self.logger = loguru.logger

    def get_token(self):
        token_url = f"{self.base_url}/get-behavior-captcha-token-v2.json?bizType=6&version=1.0&t={int(time.time() * 1000)}"
        self.logger.info(token_url)
        response = requests.get(url=token_url).json()
        data = response.get("data")
        self.logger.info(f'token is: {data.get("token")}, random str is: {data.get("randomStr")}')
        return data.get("token"), data.get("randomStr")

    def get_distance(self, youzan_token):
        distance_url = f"{self.base_url}/get-behavior-captcha-data.json?token={youzan_token}&captchaType=1&t={int(time.time() * 1000)} "
        response = requests.get(url=distance_url).json()
        data = response.get("data")
        captchaObtainInfoResult = data.get("captchaObtainInfoResult")
        bigUrl = captchaObtainInfoResult["bigUrl"]
        smallUrl = captchaObtainInfoResult["smallUrl"]
        self.logger.info(f"small url is：{smallUrl}, big url is: {bigUrl}")
        cy = captchaObtainInfoResult["cy"]
        Oorc = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        res = Oorc.slide_match(requests.get(smallUrl).content, requests.get(bigUrl).content)
        self.logger.info(f"ddddocr slider_match result is: {res}")
        value = res['target'][0]

        self.logger.info(f"x坐标：{value}, y坐标：{cy}")
        return value, cy

    @staticmethod
    def get_sign(x, y, randomStr):
        with open(r'sign.js', 'r', encoding='utf-8') as file:
            encode = execjs.compile(file.read())
        __sign = encode.call("run", int(x / 2), y, randomStr)
        return __sign

    def valid_captcha(self, token, sign):
        payload = {
            "token": token,
            "bizType": 6,
            "bizData": "",
            "captchaType": 1,
            "userBehaviorData": sign
        }
        response = requests.post(url=f"{self.base_url}/check-behavior-captcha-data.json", json=payload).json()
        self.logger.info(f"滑块验证响应：{response}")

    def run(self):
        token, randomStr = self.get_token()

        x, y = self.get_distance(token)

        sign = self.get_sign(x, y, randomStr)
        self.valid_captcha(token, sign)


if __name__ == "__main__":
    youzan = YouZanSliderCaptcha()
    youzan.run()
