from scrapy.crawler import CrawlerProcess
from .esg_spider import ESGSpider
from .configs.crawler_settings import crawler_settings
from esg_platform.sentiment_analysis.gdelt_query import gdelt_query
import logging

logger = logging.getLogger()

def crawl_urls(urls):
    process = CrawlerProcess(settings=crawler_settings)

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