# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import html2text
    # topic = scrapy.Field()
    # heading = scrapy.Field()
    # date = scrapy.Field()
    # number = scrapy.Field()
    # url = scrapy.Field()
    # body = scrapy.Field()
    # workbook = scrapy.Field()
    # sheet = scrapy.Field()
    # author = scrapy.Field()
    # directory = scrapy.Field()

class EntrepreneurPipeline(object):
    def process_item(self, item, spider):
        item['sheet'].write(item['number'], 0, item['heading'])
        item['sheet'].write(item['number'], 1, item['topic'])
        item['sheet'].write(item['number'], 2, item['date'].decode('utf-8'))
        item['sheet'].write(item['number'], 3, item['author'])
        item['sheet'].write(item['number'], 4, str(item['number'])+'.doc')
        item['sheet'].write(item['number'], 5, item['url'])
        print item['directory'] + '/' + str(item['number']) + ".doc"
        text_file = codecs.open(item['directory'] + '/' + str(item['number']) + ".doc", "w", encoding="utf-8")
        text_file.write(item['heading'])
        text_file.write('\n\n')
        h = html2text.HTML2Text()
        h.ignore_images = True
        text_file.write(h.handle(item['body']))
        text_file.close()
        item['workbook'].save(item['directory'] + "/reference.xls")
        return item
