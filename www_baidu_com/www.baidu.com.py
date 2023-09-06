#! -*-conding=: UTF-8 -*-
# 2023/9/6 16:28

# 代理简单使用

import requests


def get_ip():
    kdl_url = "https://tps.kdlapi.com/api/gettps/"
    ips = requests.get(kdl_url).json()
    for ip in ips["data"]["proxy_list"]:
        yield ip


proxy = {
    "http": "http://" + next(get_ip()),
}

rsp = requests.get("https://baidu.com", proxies=proxy)

rsp.encoding = "utf-8"
print(rsp.text)

if __name__ == '__main__':
    pass
