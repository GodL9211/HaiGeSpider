#!usr/bin/env python
# -*- coding:utf-8 _*-
# __author__：lianhaifeng
# __time__：2024/6/1 8:59
import requests

cookies = {
    'tk': '-5621756640779912732',
    'sessionid': 'qdlnifuic3h3iygdq3rcaoxpyrdo9c82',
    'no-alert3': 'true',
    'm': '3d3639f9eb1db367d6019b3ec415552e|1717231708000',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh',
    'cache-control': 'no-cache',
    # 'cookie': 'tk=-5621756640779912732; sessionid=qdlnifuic3h3iygdq3rcaoxpyrdo9c82; no-alert3=true; m=7c5827c444f0e95d6579d6e8c13ea58c|1717231248000',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/2',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'page': '2',
}

response = requests.get('https://match.yuanrenxue.cn/api/match/2', params=params, cookies=cookies, headers=headers)

print(response.json())