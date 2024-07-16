#!usr/bin/env python
# -*- coding:utf-8 _*-
# coding:utf-8
import requests
import time
import execjs


def get_time():
    now = int(time.time()) * 1000
    print(now)
    return now


cookies = {
    'tk': '-5621756640779912732',
    'sessionid': 'qdlnifuic3h3iygdq3rcaoxpyrdo9c82',
    'no-alert3': 'true',
    'm': '3d3639f9eb1db367d6019b3ec415552e|1717231708000',
}


def js_m(timestamp):
    js_txt = open('最终.js', 'r', encoding='utf-8').read()
    js_complie = execjs.compile(js_txt)
    m = js_complie.call('get_m', str(timestamp))
    print(m)
    return m


def yuanrenxue_sprider(m, page):
    url = 'https://match.yuanrenxue.com/api/match/2?page={page}'.format(page=page)
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.10 Safari/537.36',
    }
    cookies['m'] = m
    response = requests.get(url, headers=headers,  cookies=cookies,  verify=False)
    res = response.json()
    for i in res['data']:
        data = i['value']
        ticket_lists.append(data)


if __name__ == '__main__':
    ticket_lists = []
    timestamp = get_time()
    cookie = js_m(timestamp)
    for i in range(1, 6):
        yuanrenxue_sprider(cookie, i)
    print(ticket_lists)
    average = sum(ticket_lists)
    print('热度的总值为：', average)
