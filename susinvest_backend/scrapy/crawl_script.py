from scrapy.crawler import CrawlerProcess
from .esg_spider import ESGSpider
from .configs.crawler_settings import crawler_settings
from susinvest_backend.sentiment_analysis.gdelt_query import gdelt_query
import logging

logger = logging.getLogger()

def crawl_urls(urls, corpus):
    process = CrawlerProcess(settings=crawler_settings)

    process.crawl(ESGSpider, urls=urls, corpus=corpus)
    process.start() # the script will block here until the crawling is finished

def crawl_query(query_str, corpus='environmental', max_crawl=None):
    '''
    The main function of the backend. Returns a score for the query based on the corpus used.

    query_str: String to query GDELT for articles. Generally will be the company to analyse for ESG.

    corpus: Preferred corpus to use. Three corpuses have been curated (environmental, social, governance). Defaults to 'environmental'.

    max_crawl: Limits the number of GDELT articles crawled by the Scrapy spider. For debug purposes only.
    '''
    urls = gdelt_query(query_str)
    max_crawl = -1 if max_crawl == None else max_crawl
    if max_crawl > 0 and max_crawl <= len(urls):
        crawl_urls(urls[:max_crawl], corpus)
    else:
        if max_crawl > len(urls):
            logger.info("Max crawl exceeds URL list length. Defaulting to max_crawl=None.")
        crawl_urls(urls, corpus)