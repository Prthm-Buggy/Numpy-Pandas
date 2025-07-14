import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"  # <- THIS is the spider name you must match when running
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").get(),
                'author': quote.css("small.author::text").get(),
                'tags': quote.css("div.tags a.tag::text").getall(),
            }
