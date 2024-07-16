#!usr/bin/env python
# -*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2024/6/1 11:02


import requests

cookies = {
    'tk': '-5621756640779912732',
    'sessionid': 'qdlnifuic3h3iygdq3rcaoxpyrdo9c82',
    'qpfccr': 'true',
    'no-alert3': 'true',
    # "m": "bc6b271c56b8b9d0a17a93b8bea6b28|1717231079000"
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh',
    'cache-control': 'no-cache',
    # 'cookie': 'tk=-5621756640779912732; sessionid=qdlnifuic3h3iygdq3rcaoxpyrdo9c82; qpfccr=true; no-alert3=true; m=bc6b271c56b8b9d0a17a93b8bea6b28|1717231079000',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/2',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

response = requests.get('https://match.yuanrenxue.cn/match/2', cookies=cookies, headers=headers)

print(response.text)

# with open('2_原始.js', 'w', encoding='utf-8') as f:
#     f.write(response.text)