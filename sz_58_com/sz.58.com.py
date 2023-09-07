#! -*-conding=: UTF-8 -*-
# 2023/9/7 13:37
import asyncio
import json
import random

import requests
from lxml import etree

import urllib3  # 禁用安全请求警告,当目标使用htpps时使用

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

url = 'https://sz.58.com/ershoufang/p%d/?PGTID=0d30000c-0000-2e04-d18a-9af183e2d6a4&ClickID=1'


async def download(img_url):
    """
    有限速..系统检测到您疑似使用网页抓取工具访问本网站,请卸载删除后访问,ip:183.yy.xxx.145
    """
    await asyncio.sleep(random.randint(10, 20))
    response = requests.get(url=img_url, headers=headers, verify=False)
    page_text = response.text
    print(page_text)

    tree = etree.HTML(page_text)
    print("----" * 10)

    tongji_list = tree.xpath('//section[@class="list"]/div')
    print(tongji_list)

    with open('58.csv', 'w', encoding='utf-8') as f:
        for index, li in enumerate(tongji_list):
            print(index, li)

            title = li.xpath(f'./a/div[2]//h3/text()')[0]
            print(title)

            total_price = li.xpath('./a/div[2]/div[2]/p[1]/span[1]/text()')[0]
            price = li.xpath('./a/div[2]/div[2]/p[2]/text()')[0]
            details = {
                "标题": title,
                "总价": total_price + "万",
                "单价": price
            }
            f.write(json.dumps(details, ensure_ascii=False) + '\n')


async def main():
    urls = [
        url
    ]
    tasks = []
    for _url in urls:
        task = asyncio.create_task(download(_url))
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

"""
有限速..系统检测到您疑似使用网页抓取工具访问本网站,请卸载删除后访问,ip:183.17.228.145
"""
