# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #用户名
    user_name = scrapy.Field()
    #个人主页
    user_home = scrapy.Field()
    #部门
    user_department = scrapy.Field()
    #职位
    user_position = scrapy.Field()
    #回答问题数
    answer_num = scrapy.Field()
    #被赞同数
    agree_num = scrapy.Field()
    #被感谢数
    thanks_num = scrapy.Field()


