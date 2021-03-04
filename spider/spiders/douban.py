import scrapy
import json
from spider.items import Movie

class Douban(scrapy.Spider):
    name = 'douban'

    def start_requests(self):
        self.base_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0%2C10&tags=%E5%8A%B1%E5%BF%97&start={}'

        self.offset = 0
        yield scrapy.Request(self.base_url.format(0), callback=self.parse)

    def parse(self, response):
        json_body = json.loads(response.body_as_unicode())
        # analyse and yield the item
        for i in range(0, 20):
            item = self.analyze(json_body['data'][i])
            yield item
        # after that, get the next link, and yield the request

        self.offset += 20
        next_url = self.nexturl()
        yield scrapy.Request(url=next_url, callback=self.parse)

    def analyze(self, json_data: dict):
        item = Movie()
        item['casts'] = json_data['casts']
        item['cover_url'] = json_data['cover']
        item['directors'] = json_data['directors']
        item['rate']  = json_data['rate']
        item['star']  = json_data['star']
        item['title'] = json_data['title']

        return item

    def nexturl(self):
        return self.base_url.format(self.offset)
        
