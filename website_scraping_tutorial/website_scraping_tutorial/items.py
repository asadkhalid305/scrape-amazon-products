# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebsiteScrapingTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    owner = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
