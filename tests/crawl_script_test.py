import sys
import os

# Ensures that the susinvest path is added to PYTHONPATH as a module for importing
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit('\\', 1)[0])

from investdjango.susinvest.scripts.scrapy.crawl_script import crawl_query

if __name__ == "__main__":
    crawl_query("exxon", "social", max_crawl=None)