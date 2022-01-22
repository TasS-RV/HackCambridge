import logging
import re
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class CrawlSpider(scrapy.Spider):
    name = "quotes"
    rules = (Rule(LinkExtractor(
        deny=[
                re.escape('*/offsite'),
                re.escape('*/whitelist-offsite'),
            ],
    )),)

    def __init__(self, url):
        self.start_urls = [url]
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        return response.body