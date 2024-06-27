#! -*-conding=: UTF-8 -*-
# 2024/6/25 14:09

import requests

cookies = {
    '__jsluid_s': '4f1700d1468ac87204491b9c698e1835',
    'JSESSIONID': '6DE0FE52A86C8882A82955A70F4D1F6F',
    '__jsl_clearance_s': '1719295803.967|-1|jWZhPcy519vTSxv051rX2AgH8ws%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '__jsluid_s=4f1700d1468ac87204491b9c698e1835; JSESSIONID=6DE0FE52A86C8882A82955A70F4D1F6F; __jsl_clearance_s=1719295803.967|-1|jWZhPcy519vTSxv051rX2AgH8ws%3D',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnvd.org.cn/flaw/typelist?typeId=27',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'typeId': '27',
}

response = requests.get('https://www.cnvd.org.cn/flaw/typelist', params=params, cookies=cookies, headers=headers)
print(response.text)