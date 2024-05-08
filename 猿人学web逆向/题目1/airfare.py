#! -*-conding=: UTF-8 -*-
# 2024/5/8 15:06


import requests

cookies = {
    'tk': '7699535563564611254',
    'sessionid': '0qtsyidunti3daajuz7l2qkqy3m0knmd',
}

headers = {
    'authority': 'match.yuanrenxue.cn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'tk=7699535563564611254; sessionid=0qtsyidunti3daajuz7l2qkqy3m0knmd',
    'pragma': 'no-cache',
    'referer': 'https://match.yuanrenxue.cn/match/1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'page': '3',
    'm': '2ae2b736fe6fe5b74675348184f0a49a丨1715251891',
}


for i in range(1, 6):
    params["page"] = i
    response = requests.get('https://match.yuanrenxue.cn/api/match/1', params=params, cookies=cookies, headers=headers)
    print(response.json())