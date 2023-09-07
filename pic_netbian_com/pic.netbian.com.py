#! -*-conding=: UTF-8 -*-
# 2023/9/7 11:30
import random
import time

import requests
from lxml import etree

import urllib3  # 禁用安全请求警告,当目标使用htpps时使用
import os
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')

url = 'https://pic.netbian.com/4kmeinv/index_%d.html'


def download(img_url):
    time.sleep(random.randint(2, 20))
    response = requests.get(url=img_url, headers=headers, verify=False)
    page_text = response.text
    print(page_text)
    tree = etree.HTML(page_text)
    # 解析src的属性值，解析alt属性值
    li_list = tree.xpath('//div[@class="wrap clearfix"]//li')
    for li in li_list:
        src = '	https://pic.netbian.com' + li.xpath('./a/img/@src')[0]

        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 解决中文乱码的方法
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        print(src, img_name)
        with open(f"./picLibs/{img_name}", "wb") as f:
            img_data = requests.get(src, headers=headers).content
            f.write(img_data)
            print("--------------------下载成功！！----------------------------")


if __name__ == '__main__':
    with ThreadPoolExecutor(20) as t:
        # urls = [format(url % i) for i in range(2, 20)]
        urls = [format(url % i) for i in range(2, 3)]
        t.map(download, urls)  # 将文件f传递给download函数
