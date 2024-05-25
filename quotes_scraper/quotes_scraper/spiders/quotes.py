from scrapy import Spider, Request

from quotes_scraper.items import AuthorItem, QuoteItem
from quotes_scraper.pipelines import QuotesScraperPipeline


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com']
    custom_settings = {"ITEM_PIPELINES": {QuotesScraperPipeline: 300}}

    def parse(self, response):
        for quote_response in response.xpath('/html//div[@class="quote"]'):
            quote = quote_response.xpath('span[@class="text"]/text()').get().strip()
            author = quote_response.xpath('span/small[@class="author"]/text()').get().strip()
            tags = quote_response.xpath('div[@class="tags"]/a/text()').getall()
            tags = [tag.strip().lower() for tag in tags]

            yield QuoteItem(tags=tags, author=author, quote=quote)
            yield response.follow(
                url=self.start_urls[0] + quote_response.xpath('span/a/@href').get(), callback=self.parse_author
            )

        next_link = response.xpath('//li[@class="next"]/a/@href').get()

        if next_link:
            yield Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        author_response = response.xpath('//div[@class="author-details"]')
        name = author_response.xpath('//h3[@class="author-title"]/text()').get().strip()
        born_date = author_response.xpath('//span[@class="author-born-date"]/text()').get().strip()
        born_location = author_response.xpath('//span[@class="author-born-location"]/text()').get().strip()
        description = author_response.xpath('//div[@class="author-description"]/text()').get().strip()

        yield AuthorItem(name=name, born_date=born_date, born_location=born_location, description=description)
