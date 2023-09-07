#! -*-conding=: UTF-8 -*-
# 2023/9/7 17:58
# -*- coding: UTF-8 -*-
# 2023/9/7 17:58
import asyncio
import aiohttp
import aiofiles
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


async def download(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            page_text = await resp.content.read()
            print(resp.status)
            print(page_text)

            tree = etree.HTML(page_text)
            li_list = tree.xpath('//div[@class="wrap clearfix"]//li')
            print(url)
            print(li_list)

    for li in li_list:
        src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        print(src, img_name)

        async with aiofiles.open(img_name, mode="wb") as f:
            async with session.get(src) as img_resp:
                content = await img_resp.content.read()
                await f.write(content)


async def main():
    _url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    url_list = [
        _url % i for i in range(2, 20)
    ]
    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    _main = main()
    asyncio.run(_main)
