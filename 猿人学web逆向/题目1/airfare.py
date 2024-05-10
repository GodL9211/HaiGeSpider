#! -*-conding=: UTF-8 -*-
# 2024/5/8 15:06

import execjs
import requests

import pandas as pd

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
    'page': 1,
    'm': '',
}


def calculate_m_value():
    with open('_m.js', mode='r', encoding='utf-8') as f:
        JsData = f.read()
    m_value = execjs.compile(JsData).call('get_m_value')
    # m_value_process = m_value.replace("丨", "%E4%B8%A8")
    return m_value


def main() -> int:
    _sum = 0
    times = 0
    df = pd.DataFrame()
    for page_number in range(1, 6):
        params["page"] = page_number
        params["m"] = calculate_m_value()
        print(params)
        response = requests.get('https://match.yuanrenxue.cn/api/match/1', params=params, cookies=cookies,
                                headers=headers).json()
        # print(response)
        df = pd.concat([df, pd.DataFrame(response["data"])], ignore_index=True)
        for data in response["data"]:
            _sum += data["value"]
            times += 1

    print(df.values.mean())
    if not times:
        return 0

    return int(_sum / times)


if __name__ == "__main__":
    result = main()
    print(int(result))
