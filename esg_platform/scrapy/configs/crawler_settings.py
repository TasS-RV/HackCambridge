crawler_settings = {
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
}