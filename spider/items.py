# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ShitItem(scrapy.Item):
    author = scrapy.Field()
    gender = scrapy.Field()
    age    = scrapy.Field()
    text   = scrapy.Field()
    laugh  = scrapy.Field()

    
