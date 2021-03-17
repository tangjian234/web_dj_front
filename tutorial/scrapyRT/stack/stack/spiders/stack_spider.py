from scrapy import Spider
from scrapy.selector import Selector
import scrapy
from scrapy.item import Item, Field

from log_lib import Logger
logger = Logger()

class StackItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    def __init__(self,  asin_list= 'A-S'):
        #self.first = first  # source file name
        asin_list=asin_list.replace(' ', '').split(";")
        header="https://www.amazon.com/dp/" 
        self.remote_urls= [header+asin for asin in asin_list]
        print(self.remote_urls)
                

    def parse(self, response):
        logger.worker.warning("run stack once")

        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
