# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ShitPipeline:
    def __init__(self):
        self.folder = '/home/steiner/spider/storage/'
        self.path   = self.folder + 'shit'
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
            
        self.format = ("author: {}\n"
                       "gender: {}\n"
                       "age   : {}\n"
                       "text  : {}\n"
                       "laugh : {}\n")

    def process_item(self, item, spider):
        with open(self.path, 'a') as f:
            content = self.format.format(item['author'],
                                         item['gender'],
                                         item['age'],
                                         item['text'],
                                         item['laugh'])
            f.writelines(content)
            f.write('\n')

