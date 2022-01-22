from scrapy.crawler import CrawlerProcess
from .crawl_spider import CrawlSpider

process = CrawlerProcess(settings={
    "BOT_NAME": "crawlbot",
    "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7", # Random
    "ROBOTSTXT_OBEY": False,
    "CONCURRENT_REQUESTS": 32,
    "CONCURRENT_ITEMS": 100,
    "DOWNLOAD_DELAY": 0.26,
    "COOKIES_ENABLED": False
})

process.crawl(CrawlSpider, url="https://www.cambridgesu.co.uk/")
process.start() # the script will block here until the crawling is finished