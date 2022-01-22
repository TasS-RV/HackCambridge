import logging
from scrapy import Spider, Request

logger = logging.getLogger()

class ESGSpider(Spider):
    name = "quotes"

    def __init__(self, urls):
        self.start_urls = urls
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        return {'content': response.css("p::text").getall()}