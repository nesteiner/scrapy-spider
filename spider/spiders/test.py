import scrapy

class Test(scrapy.Spider):
    name = 'test'
    
    def start_requests(self):
        self.base_url = 'http://exercise.kingname.info/exercise_middleware_ua/{}'
        self.offset = 1

        yield scrapy.Request(url = self.base_url.format(self.offset), callback = self.parse)

    def parse(self, response):
        yield {'text': response.body_as_unicode()}

        if self.offset <= 10:
            self.offset += 1
            yield scrapy.Request(url=self.base_url.format(self.offset), callback = self.parse)
