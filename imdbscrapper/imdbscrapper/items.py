# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	#pass
	name = scrapy.Field()
	year = scrapy.Field()
	imdb_rating = scrapy.Field()
	imdb_url = scrapy.Field()
	imdb_img = scrapy.Field()
	rt_critic_rating = scrapy.Field()
	rt_audience_rating = scrapy.Field()
	rt_url = scrapy.Field()
	genre1 = scrapy.Field()
	genre2 = scrapy.Field()
	genre3 = scrapy.Field()
	duration = scrapy.Field()