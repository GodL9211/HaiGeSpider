#! -*-conding=: UTF-8 -*-
# 2024/5/21 19:44

"""
b站视频标题的获取（xpath）
"""
import json
import random
import urllib.request
import gzip
import io

import jsonpath
from lxml import etree
from loguru import logger

# 请求头
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    # 'cookie': "buvid3=FF1F9696-382C-F163-36C0-0D6EFAF8038115443infoc; b_nut=1714457615; CURRENT_FNVAL=4048; _uuid=5101A82A9-A84D-4697-1CB9-CC37E14D5102D30615infoc; buvid_fp=696e07e6f38e26510e91d64f4af96672; buvid4=83762567-FE3D-9711-7684-2D10E720132569145-024031803-spGqFTsMy2+0JdzkvGUv5Q%3D%3D; rpdid=|(J|~uR|Jlk)0J'u~uRRl~Yu~; DedeUserID=291280839; DedeUserID__ckMd5=dff1294a97029627; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=0; browser_resolution=1858-959; PVID=1; bp_t_offset_291280839=932004845266665558; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY1Mjk1NjMsImlhdCI6MTcxNjI3MDMwMywicGx0IjotMX0.MfQ7r1tK8j_Jmf9YJA-UuT9blbwJv5D_Zy_owdYlwQ4; bili_ticket_expires=1716529503; SESSDATA=d780ed53%2C1731822368%2C7ccc4%2A51CjB7NpyE-4cm7rIge2bjGMBqJQli5zroGFIWQnRjkDlvkLReabDn23SHCLueWxhM0LsSVldtSVRsOFhDdkdrSGVCbXFMVlJIa2YwOWZ1R3h3NklqNjhZSnhPZVl5MlNMS2Y4c01GVzZsamhGWjltRDZhX0NJaXNySERObnpkVnNyaXc2WW9yQklBIIEC; bili_jct=cdee0e3875896c84e93495e0b5cbb5b7; b_lsid=F2892C9E_18F9A55C8BD; sid=8m9ie19f",
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'priority': 'u=4, i',
    'referer': 'https://www.bilibili.com/video/BV1g1421676B/?vd_source=f6ed028b29a932df5d0a09a54802e1b5',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


def fetch_and_decompress_url(url):
    """
    Fetches and decompresses the content of a URL.

    Parameters:
    - url (str): The URL to fetch.
    - headers (dict): The headers to use for the request.

    Returns:
    - str: The decompressed content of the URL.
    """
    # 创建请求对象
    request = urllib.request.Request(url=url, headers=headers)

    # 发送请求并获取响应
    with urllib.request.urlopen(request) as response:
        # 读取响应内容
        content_bytes = response.read()

        # 解压并解码内容
        content_io = io.BytesIO(content_bytes)
        with gzip.GzipFile(fileobj=content_io, mode='rb') as f:
            content_ = f.read().decode('utf-8')

    return content_


# logger.info(content)
def save_html(_content):
    # # 将网页源码保存到文件“b站视频标题的获取（xpath）.html”中
    if _content.find("latex03-LaTeX中的中文处理方法") != -1:
        title = "LaTeX视频合集"
    elif _content.find("李清照") != -1:
        title = "宋词宋史宋朝"
    else:
        title = "dnf合集"
    with open(f'{title}的获取（xpath）.html', 'w', encoding='UTF-8') as fp:
        fp.write(_content)


def parse_response(_content):
    # 2.获取视频标题
    # （1）处理变成json数据
    # 解析服务器响应的文件  etree.HTML
    tree = etree.HTML(_content)
    # 获取想要的数据
    # 失败路径，需要将网页源码导入html文件中，手动找  /html/body/div[2]/div[2]/div[2]/div/div[7]/div[2]/ul/li/a/div/div[1]/span[2]/text()
    the_data = tree.xpath('/html/head[@itemprop="video"]/script[5]/text()')[0]  # 由于tree.xpath返回的是列表，需要使用切片[0]将它取出来
    # print(the_data)  # 测试代码，验证xpath路径是否正确
    the_json_data = the_data.split('__=')[1].split(';(function')[0]
    # print(the_json_data)  # 测试代码，验证得到的json数据是否正确
    # （2）处理json数据，得到视频的标题
    # # 法1.使用切片
    # # 将字符串json转换为python的字典
    # data_dict = json.loads(the_json_data)
    #
    # # 根据json数据的层次结构获取视频的标题
    # the_temp_data = data_dict['videoData']['pages']
    # the_name_of_videos = []  # 用于存储视频的标题
    # for name in the_temp_data:
    #     the_name_of_videos.append(name['part'])
    # 法2.使用jsonpath解析
    the_pages_of_videos = jsonpath.jsonpath(json.loads(the_json_data), '$.videoData.pages[*]')
    logger.info(the_pages_of_videos)

    the_name_of_videos = jsonpath.jsonpath(json.loads(the_json_data),
                                           '$.videoData.ugc_season.sections[*].episodes[*].arc.title')

    if not the_name_of_videos:
        the_name_of_videos = jsonpath.jsonpath(json.loads(the_json_data), '$.videoData.pages[*].part')
        logger.debug("从part中获得合集信息")
    else:
        logger.debug("从ugc_season中获得合集信息")
    # 打印b站视频的标题
    for name in the_name_of_videos:
        logger.info(name)


if __name__ == '__main__':
    # 请求地址
    urls = [
        'https://www.bilibili.com/video/BV1g1421676B/?vd_source=f6ed028b29a932df5d0a09a54802e1b5',
        "https://www.bilibili.com/video/BV15b411j7Au/?vd_source=ffb19c330efa",
        "https://www.bilibili.com/video/BV1rk4y1a7ii/?&vd_source=f6ed028b29a932df5d0a09a54802e1b5"
    ]
    # 获取并打印内容
    content = fetch_and_decompress_url(random.choice(urls))

    save_html(content)

    parse_response(content)
