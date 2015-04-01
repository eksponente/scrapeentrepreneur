# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
# from scrapy.item import Item, Field


class ArticleItem(scrapy.Item):
    topic = scrapy.Field()
    heading = scrapy.Field()
    date = scrapy.Field()
    number = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    workbook = scrapy.Field()
    sheet = scrapy.Field()
    author = scrapy.Field()
    directory = scrapy.Field()
