from scrapy.crawler import CrawlerProcess
from .esg_spider import ESGSpider
from esg_platform.sentiment_analysis.gdelt_query import gdelt_query
import logging

logger = logging.getLogger()

def crawl_urls(urls):
    process = CrawlerProcess(settings={
        "BOT_NAME": "esgcrawlbot",
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7", # Random
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS": 32,
        "CONCURRENT_ITEMS": 100,
        "DOWNLOAD_DELAY": 0.26,
        "COOKIES_ENABLED": False,
        "ITEM_PIPELINES": {
            "esg_platform.scrapy.item_pipelines.ESGCrawlPipeline": 100
        }
    })

    process.crawl(ESGSpider, urls=urls)
    process.start() # the script will block here until the crawling is finished

def crawl_query(query_str, max_crawl=None):
    urls = gdelt_query(query_str)
    max_crawl = -1 if max_crawl == None else max_crawl
    if max_crawl > 0 and max_crawl <= len(urls):
        crawl_urls(urls[:max_crawl])
    else:
        if max_crawl > len(urls):
            logger.info("Max crawl exceeds URL list length. Defaulting to max_crawl=None.")
        crawl_urls(urls)