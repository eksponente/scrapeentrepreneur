import sys
sys.path.append('/home/eksponente/Downloads/cx_Freeze-4.3.3/')
from cx_Freeze import setup, Executable

setup(name='Article Scraper',
	version='1.0',
	description='Use this program to scrape articles from entrepreneur.com',
	executables = [Executable("article_spider.py")])
