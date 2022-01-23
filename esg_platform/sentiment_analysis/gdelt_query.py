import datetime
from gdeltdoc import GdeltDoc, Filters
import logging

logger = logging.getLogger()

def date_to_str(date):
    return str.split(str(date), " ")[0]

def gdelt_query(query_str):
    now = date_to_str(datetime.datetime.now())
    start_date = date_to_str(datetime.datetime.now() - datetime.timedelta(days=90)) # Get news up to 3 months ago

    f = Filters(
        keyword = query_str, # Must have a length of 5 characters or more
        start_date = start_date,
        end_date = now
    )

    logger.info(f"GDELT Query: {query_str}")

    gd = GdeltDoc()

    articles = gd.article_search(f)

    return articles[articles["language"]=='English']['url'].to_list()