import scrapy
from spider.items import ShitItem

class Shit(scrapy.Spider):
    name = 'shit'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        count = 1
        while count <= 10:
            count += 1
            self.parse_onepage(response)
            next_url = self.parse_next_url(response)
            yield scrapy.Request(url=next_url, callback=self.parse_onepage)


    def parse_onepage(self, response):
        product = ShitItem()
        for selector in response.css('div.article.block.untagged.mb15'):
            product['author']    = selector.css('div.author.clearfix h2::text').extract_first().replace('\n', '')
            product['gender']  = selector.css('div.articleGender::attr(class)').extract_first().split(' ')[1]

            product['age']     = selector.css('div.author.clearfix > div.articleGender::text').extract_first().replace('\n', '')
            product['text'] = selector.css('div.content span::text').extract_first().replace('\n', '')
            product['laugh']   = selector.css('div.stats i.number::text').extract_first().replace('\n', '')

            yield product


    def parse_next_url(self, response):
        for selector in response.css('ul.pagination li a'):
            if not selector.css('span.next::text').extract_first() == None:
                return response.urljoin(selector.attrib['href'])
   
