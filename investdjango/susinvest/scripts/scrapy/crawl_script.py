from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from multiprocessing import Process, Queue
from uuid import uuid4
from .esg_spider import ESGSpider
from .configs.crawler_settings import crawler_settings
from ..gdelt.gdelt_query import gdelt_query
import logging

logger = logging.getLogger()

# For multi-processing (and running the reactor more than once)
def crawl_core(q, urls, corpus):
    try:
        runner = CrawlerRunner(settings=crawler_settings)
        deferred = runner.crawl(ESGSpider, urls=urls, corpus=corpus)
        deferred.addBoth(lambda _: reactor.stop())
        reactor.run()#installSignalHandlers=False)
        q.put(None)
    except Exception as e:
        q.put(e)

def crawl_urls(urls, corpus, uid):
    crawler_settings["uid"] = uid

    q = Queue()
    p = Process(target=crawl_core, args=(q, urls, corpus,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result

def crawl_query(query_str, corpus='environmental', uid=0, max_crawl=None):
    '''
    The main function of the backend. Returns a score for the query based on the corpus used.

    query_str: String to query GDELT for articles. Generally will be the company to analyse for ESG.

    corpus: Preferred corpus to use. Three corpuses have been curated (environmental, social, governance). Defaults to 'environmental'.

    max_crawl: Limits the number of GDELT articles crawled by the Scrapy spider. For debug purposes only.
    '''
    urls = gdelt_query(query_str)
    logger.info('GDELT data received.')
    max_crawl = -1 if max_crawl == None else max_crawl
    if max_crawl > 0 and max_crawl <= len(urls):
        logger.info('Begin crawl.')
        crawl_urls(urls[:max_crawl], corpus, uid)
    else:
        if max_crawl > len(urls):
            logger.info("Max crawl exceeds URL list length. Defaulting to max_crawl=None.")
        logger.info('Begin crawl.')
        crawl_urls(urls, corpus, uid)