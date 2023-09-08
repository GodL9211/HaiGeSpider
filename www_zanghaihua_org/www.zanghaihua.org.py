#! -*-conding=: UTF-8 -*-
# 2023/9/8 11:42
"""
node -v
  v18.16.1
npm install puppeteer

安装chrom: playwright install

node render.js https://www.zanghaihua.org/mingchaonaxieshier/402.html
"""

import asyncio
import platform
import subprocess

import aiofiles
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


def get_chapter_url(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "gbk"
    print(resp.text)
    tree = etree.HTML(resp.text)
    href_list = tree.xpath('//*[@id="section-list"]/li/a/@href')
    print(href_list)
    return href_list


def render_page(url):
    try:
        # 使用subprocess运行Node.js脚本并捕获标准输出
        result = subprocess.run(['node', './render.js', url], capture_output=True, text=True, check=True,
                                encoding='utf-8')
        rendered_html = result.stdout

        # 返回渲染后的HTML内容
        return rendered_html
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


async def download_one(href):
    rendered_html = render_page(href)

    if rendered_html is None:
        raise ValueError("获取渲染后的HTML内容失败。")

    # 在此处处理渲染后的HTML内容
    print("渲染后的HTML内容：")
    print(rendered_html)
    tree = etree.HTML(rendered_html)

    title = tree.xpath('//*[@id="container"]/div/div/div[2]/h1/text()')[0].strip()
    content = tree.xpath('//*[@id="content"]/text()')
    print(title)
    print(content)
    content_string = "\n".join(content).replace("\u3000", "")
    async with aiofiles.open(f"./明朝那些事儿/{title}.txt", mode="w", encoding="utf-8") as f:
        await f.write(content_string)
    print(f"{title}下载完毕！！")


async def download(url_list):
    tasks = []
    for href in url_list:
        t = asyncio.create_task(download_one(href))
        tasks.append(t)
    await asyncio.gather(*tasks)


# 主函数
def main():
    # url = 'https://www.zanghaihua.org/mingchaonaxieshier/402.html'  # 您要渲染的网页URL
    url_list = get_chapter_url("https://www.zanghaihua.org/mingchaonaxieshier/")
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(download(url_list[0:2]))


if __name__ == "__main__":
    main()
