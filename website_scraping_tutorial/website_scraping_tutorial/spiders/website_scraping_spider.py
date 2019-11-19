# -*- coding: utf-8 -*-
from urllib import response

import scrapy
from ..items import WebsiteScrapingTutorialItem


class WebsiteScrapingSpiderSpider(scrapy.Spider):
    name = 'website_scraping_spider'
    pageNo = 2
    start_urls = [
        'https://www.amazon.com/s?i=specialty-aps&bbn=16225008011&rh=n%3A%2116225008011%2Cn%3A5223262011&ref=nav_em_T1_0_4_NaN_14__nav_desktop_sa_intl_programming_web_development']

    def parse(self, response):
        items = WebsiteScrapingTutorialItem()

        items['title'] = response.css('.a-color-base.a-text-normal').css('::text').extract()
        items['owner'] = response.css('.sg-col-12-of-28 .a-color-secondary span').css('::text').extract()
        items['image'] = response.css('.s-image::attr(src)').extract()
        items['price'] = response.css(
            '.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()

        yield items

        next_page = 'https://www.amazon.com/s?i=software-intl-ship&bbn=16225008011&rh=n%3A16225008011%2Cn%3A5223262011&page=' + str(
            WebsiteScrapingSpiderSpider.pageNo) + '&qid=1574091842&ref=sr_pg_2'

        if WebsiteScrapingSpiderSpider.pageNo <= 10:
            WebsiteScrapingSpiderSpider.pageNo += 1
            yield response.follow(next_page, callback=self.parse)
