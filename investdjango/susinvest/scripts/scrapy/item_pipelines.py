import string
import numpy as np
from scipy.special import expit
from .configs.weighted_corpus import corpus
from ...models import ESGModel
from twisted.internet import reactor

import logging

logger = logging.getLogger()

class ESGCrawlPipeline:

    def __init__(self, uid):
        self.punctuation = string.punctuation.strip('"').strip("'").strip('-')
        self.words = []
        self.uid = uid

    @classmethod
    def from_crawler(cls, crawler): # Constructor from crawler
        return cls(
            uid=crawler.settings.get('uid'), # this will be passed from django view
        )

    def process_item(self, item, spider):
        words = [
            word.strip('\n').strip('\t')
                for paragraph in item['content']
                for word in str.split(paragraph.translate(str.maketrans('', '', self.punctuation)))
        ]
        self.words = self.words + words
        return words

    
    def close_spider(self, spider):
        data = np.char.lower(np.array(self.words))
        unique, counts = np.unique(data, return_counts=True)
        word_counts = dict(zip(unique, counts))

        score = 0 # Scoring the company

        for k, v in corpus[spider.corpus]["words"].items():
            if k in word_counts:
                score += word_counts[k] * v

        normalise_factor = corpus[spider.corpus]["normalise_factor"]
        score = expit(score/normalise_factor) # Sigmoid

        try:
            item = ESGModel.objects.get(uid=self.uid)
        except:
            logger.info('Instance does not exist. Creating instance.')
            item = ESGModel()
        item.uid = self.uid
        item.data = str(score)
        item.save()