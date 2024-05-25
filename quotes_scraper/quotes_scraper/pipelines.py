# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesScraperPipeline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if 'name' in adapter.keys():
            self.authors.append(dict(adapter))

        if 'quote' in adapter.keys():
            self.quotes.append(dict(adapter))

    def close_spider(self, spider):
        with open('data/quotes.json', 'w', encoding='utf-8') as file_descriptor:
            json.dump(self.quotes, file_descriptor, ensure_ascii=False, indent=2)

        with open('data/authors.json', 'w', encoding='utf-8') as file_descriptor:
            json.dump(self.authors, file_descriptor, ensure_ascii=False, indent=2)

