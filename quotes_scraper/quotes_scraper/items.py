# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class QuoteItem(Item):
    quote = Field()
    author = Field()
    tags = Field()


class AuthorItem(Item):
    name = Field()
    born_date = Field()
    born_location = Field()
    description = Field()
