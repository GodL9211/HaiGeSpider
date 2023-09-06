#! -*-conding=: UTF-8 -*-
# 2023/9/6 17:59

import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://www.xinfadi.com.cn/getPriceData.html"


def download(url, f, current=1, limit=20):
    resp = requests.post(url=url, data={"limit": limit, "current": current}).json()
    # 将响应内容以字符串形式写入CSV文件
    f.write(str(resp))
    f.write("\n")


if __name__ == '__main__':
    # 使用with语句来自动关闭文件
    with open("xinfadi.csv", mode="w", encoding="utf-8") as f:
        with ThreadPoolExecutor(20) as t:
            # 方式一、一次性构造不同的URL并提交给线程池
            urls = [url] * 10  # 重复10次以创建10个不同的URL
            t.map(download, urls, [f] * len(urls), [i for i in range(1, 10)])  # 将文件f传递给download函数
            # 方式二、自己循环提交任务到线程池
            # for i in range(1, 10):
            #     t.submit(download, url, f, current=i)
