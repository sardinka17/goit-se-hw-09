from pathlib import Path

from scrapy.crawler import CrawlerProcess

from quotes_finder.connect import connect_to_db
from quotes_finder.parse_command import find_quotes_by_author, find_quotes_by_tags
from quotes_finder.seeds import save_authors_to_db, save_quotes_to_db
from quotes_scraper.spiders.quotes import QuotesSpider

if __name__ == '__main__':
    Path("data").mkdir(parents=True, exist_ok=True)
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
    connect_to_db()
    save_authors_to_db()
    save_quotes_to_db()

    while True:
        command = input(str('Enter a command: '))

        if 'name' in command:
            cmd, first_name, last_name = command.split(' ')
            name = f'{first_name} {last_name}'
            print(find_quotes_by_author(name))
        elif 'tags' in command:
            cmd, tags = command.split(':')
            print(find_quotes_by_tags(tags))
        elif 'tag' in command:
            cmd, tags = command.split(':')
            print(find_quotes_by_tags(tags))
        elif 'exit' in command:
            print('Good bye!')
            break
        else:
            print('Command is invalid! Please, try again.')
