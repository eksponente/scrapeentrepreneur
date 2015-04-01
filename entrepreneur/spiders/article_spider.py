import scrapy
from scrapy.item import Item, Field
from scrapy.http import Request
from entrepreneur.items import ArticleItem
import html2text
import os
import xlwt
import codecs

globvar = 0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Articles")
sheet.write(0, 0, 'Article Title')
sheet.write(0, 1, 'Category')
sheet.write(0, 2, 'Date')
sheet.write(0, 3, 'Writer')
sheet.write(0, 4, 'Filename')
sheet.write(0, 5, 'URL')

class ArticleSpider(scrapy.Spider):
	name = "article"
	allowed_domains = ["entrepreneur.com"]
	start_urls = [
		"http://www.entrepreneur.com"
	]
	def parse(self, response):
		dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
		directory = os.path.join(dir, 'articles')
		if not os.path.exists(directory):
			os.makedirs(directory)
		topic_urls = [
			"http://www.entrepreneur.com/topic/leadership",
			"http://www.entrepreneur.com/topic/growth-strategies",
			"http://www.entrepreneur.com/topic/marketing",
			"http://www.entrepreneur.com/topic/technology",
			"http://www.entrepreneur.com/topic/social-media",
			"http://www.entrepreneur.com/topic/finance",
			"http://www.entrepreneur.com/topic/entrepreneurs",
			"http://www.entrepreneur.com/topic/starting-a-business",
		]
		topics = [
			"Leadership",
			"Growth & Strategy",
			"Marketing",
			"Technology",
			"Social Media",
			"Finance",
			"Entrepreneurs",
			"Starting a Business"
		]

		# request = Request("http://www.entrepreneur.com/article/234070", callback=self.scrap)
		# request.meta['filename'] = "Topic"
		# request.meta['directory'] = directory
		# return request
		for i in range(8):
			request = Request(topic_urls[i], callback=self.scrap_pages)
			request.meta['filename'] = topics[i]
			request.meta['directory'] = directory
			yield request


	def scrap_pages(self, response):
		linkai = response.xpath('//noscript/div/a/text()').extract()
		sk = int(linkai[-2])
		for i in range(sk):
			request = Request(response.url + "/" + str(i+1) , callback=self.scrap_topic)
			request.meta['filename'] = response.meta['filename']
			request.meta['directory'] = response.meta['directory']
			yield request

	def scrap_topic(self, response):
		for sel in response.xpath('//a[contains(@href, "article")] | //a[contains(@href, "slideshow")]'):
			s = sel.xpath('@href').extract()
			request = Request("http://www.entrepreneur.com" + s[0] , callback=self.scrap)
			request.meta['filename'] = response.meta['filename']
			request.meta['directory'] = response.meta['directory']
			yield request

	def scrap(self, response):
		item = ArticleItem()
		global globvar
		globvar = globvar + 1
		global sheet
		item['sheet'] = sheet
		# dir = os.path.dirname(__file__)
		# directory = os.path.join(dir, 'articles')
		#
		# text_file = codecs.open(directory + '/' + str(globvar) + ".doc", "w", encoding="utf-8")
		text = response.xpath('//h1[contains(@itemprop, "headline")]/text()').extract()
		if text:
			item['heading'] = text[0].strip()
		else:
			item['heading'] = ""
			# geras = text[0].strip()
			# sheet.write(globvar, 0, geras.strip())
		item['topic'] = response.meta['filename']
		# sheet.write(globvar, 1, response.meta['filename'])
		t = response.xpath('//div[contains(@class, "article-body")]/time/text() | //div[contains(@class, "block")]/time/text()').extract()
		if t:
			item['date'] = t[0].strip()
		else:
			item['date'] = ""
			# sheet.write(globvar, 2, t[0].decode('utf-8').strip() )
		item['number'] = globvar
		# sheet.write(globvar, 4, str(globvar) + ".doc")
		item['url'] = response.url
		# sheet.write(globvar, 5, response.url)
		# sheet.write(globvar, 6, "")
		# text_file.write(text[0].strip())
		# text_file.write('\n\n')

		text = response.xpath('//div[contains(@class, "content-block")]').extract()
		item['body'] = text[0]
		# h = html2text.HTML2Text()
		# h.ignore_images = True
		# text_file.write(h.handle(text[0]))
		# text_file.close()
		author = response.xpath('//a[contains(@rel, "author")]/div/text()').extract()
		if author:
			item['author'] = author[0].strip()
		else:
			item['author'] = ""
			# sheet.write(globvar, 3, author[0].strip())
		global workbook
		item['workbook'] = workbook
		item['directory'] = response.meta['directory']
		# workbook.save(directory + "/reference.xls")
		return item
