import string

class ESGCrawlPipeline:

    def __init__(self):
        self.punctuation = string.punctuation.strip('"').strip("'")

    def process_item(self, item, spider):
        return [
            word.strip('\n')
                for paragraph in item['content']
                for word in str.split(paragraph.translate(str.maketrans('', '', self.punctuation)))
        ]