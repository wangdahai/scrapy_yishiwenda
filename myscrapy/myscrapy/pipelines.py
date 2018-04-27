# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyscrapyPipeline(object):
    def __init__(self):
        self.f = open('yishiwenda.json','a')
    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        print content
        print '************',type(content)
        self.f.write(str(content))
        return item
    def close_spider(self,spider):
        self.f.close()
