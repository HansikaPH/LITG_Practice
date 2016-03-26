#using xpath to scrape web content

from lxml import etree
import urllib2

response = urllib2.urlopen("http://docs.python-guide.org/en/latest/scenarios/scrape/")
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
title = tree.xpath('//*[@id="html-scraping"]/h1/text()')
intro = tree.xpath('//*[@id="web-scraping"]/p[1]/text()')
web_content = { "title": title, "introduction" : intro}

print web_content
