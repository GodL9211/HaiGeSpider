# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 课程名称
    title = scrapy.Field()
    # 课程url
    url = scrapy.Field()
    # 课程标题图片url
    image_url = scrapy.Field()
    # 课程描述
    introduction = scrapy.Field()
    # 学习人数
    student = scrapy.Field()

