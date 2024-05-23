import scrapy


class ImoocSpider(scrapy.Spider):
    name = "imooc"
    allowed_domains = ["www.imooc.com"]
    start_urls = ["https://www.imooc.com"]

    def parse(self, response):
        pass
