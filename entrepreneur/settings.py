# -*- coding: utf-8 -*-

# Scrapy settings for entrepreneur project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'entrepreneur'

SPIDER_MODULES = ['entrepreneur.spiders']
NEWSPIDER_MODULE = 'entrepreneur.spiders'
ITEM_PIPELINES = {
'entrepreneur.pipelines.EntrepreneurPipeline': 1
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'entrepreneur (+http://www.yourdomain.com)'
