# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Request
from myscrapy.items import MyscrapyItem

class YishiwendaSpider(scrapy.Spider):
    name = 'yishiwenda'
    allowed_domains = ['https://www.yishiwenda.com']

    offset = 1
    base_url = 'https://www.yishiwenda.com/?/people/page-'
    start_urls = ['https://www.yishiwenda.com/?/people/']
    def parse(self, response):
        node_list = response.xpath("//div[@class='aw-item']")
        item_list = []
        for node in node_list:
            # print node
            item = MyscrapyItem()
            item['user_name'] = node.xpath(".//p[@class='text-color-999 title']/a/text()").extract_first()
            item['user_home'] = node.xpath(".//p[@class='text-color-999 title']/a/@href").extract_first()
            item['user_department'] = node.xpath(".//p[@class='text-color-999 title']/span/text()").extract_first()
            item['user_position'] = node.xpath(".//p[@class='text-color-999 title']/span/text()").extract_first()
            item['answer_num'] = node.xpath(".//div[@class='meta']/span")[0].xpath(".//b/text()").extract_first()
            item['agree_num'] = node.xpath(".//div[@class='meta']/span")[1].xpath(".//b/text()").extract_first()
            item['thanks_num'] = node.xpath(".//div[@class='meta']/span")[2].xpath(".//b/text()").extract_first()
            # print item['user_name']
            # with open('username.text', 'a') as f:
            #     f.write(item['user_name'].encode('utf-8')+'\n')
            # item_list.append(item)
            yield item
        # print len(item_list)ls
        # yield Request(url='https://www.yishiwenda.com/?/people/2',callback=self.parse)
        next_page = response.xpath("//div[@class='page-control']/ul/li")
        next_tag = next_page
        next_url = ''
        for tag in next_page:
            if tag.xpath("./a/text()").extract_first() == '>':
                next_url = tag.xpath("./a/@href").extract_first()
        print next_url
        if next_url:
            yield scrapy.http.Request(url=str(next_url),callback=self.parse,dont_filter=True)#dont_filter :去重

        print 'sssssssssssss'




