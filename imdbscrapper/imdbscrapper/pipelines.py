# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class ImdbscrapperPipeline(object):
#    def process_item(self, item, spider):
#        return item

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MySQLStorePipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect('127.0.0.1', 'root', 'lpplokok', 'mysite_db', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):    
	    try:
		self.cursor.execute("""INSERT INTO imdbscrapper_data (title, year, imdb_rating, imdb_url, rt_critic_rating, rt_audience_rating, rt_url, genre1, genre2, genre3, duration, imdb_img)  
			        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
			       (item['name'], 
			        item['year'],
					item['imdb_rating'],
					item['imdb_url'],
			       	item['rt_critic_rating'],
					item['rt_audience_rating'],
					item['rt_url'],
					item['genre1'],
					item['genre2'],
					item['genre3'],
					item['duration'],
			       	item['imdb_img']))

		self.cursor.execute("""INSERT INTO tommymovies_movie (name, year, imdb_rating, imdb_url, rt_rating, rt_url, comment, imdb_img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
			       (item['name'], 
			        item['year'],
					item['imdb_rating'],
					item['imdb_url'],
					item['rt_audience_rating'],
					item['rt_url'],
					item['duration'],
					item['imdb_img']))

		new_movie_id = self.cursor.lastrowid
		spider.log('Well, here is an new movie id : %s.' % new_movie_id)
		spider.log('printing genre1:%s' % item['genre1'])
		spider.log('printing genre2: %s' % item['genre2'])
		spider.log('printing genre3: %s' % item['genre3'])
		
		if item['genre1'] is not None:
			sql = "SELECT id FROM tommymovies_category WHERE genre=%s"
			self.cursor.execute(sql,(item['genre1'],))
			results = self.cursor.fetchall()
			for row in results:
				genre1_id = row[0]
				spider.log('Well, here is an gebre1 id : %s.' % genre1_id)
			self.cursor.execute("""INSERT INTO tommymovies_movie_categories (movie_id,category_id) VALUES (%s, %s)""",
					   (new_movie_id, 
					    genre1_id))

		if item['genre2'] is not None:
			sql = "SELECT id FROM tommymovies_category WHERE genre=%s"
			self.cursor.execute(sql,(item['genre2'],))
			results = self.cursor.fetchall()
			for row in results:
				genre2_id = row[0]
				spider.log('Well, here is an gebre2 id : %s.' % genre2_id)
			self.cursor.execute("""INSERT INTO tommymovies_movie_categories (movie_id,category_id) VALUES (%s, %s)""",
					   (new_movie_id, 
					    genre2_id))

		if item['genre3'] is not None:
			sql = "SELECT id FROM tommymovies_category WHERE genre=%s"
			self.cursor.execute(sql,(item['genre3'],))
			results = self.cursor.fetchall()
			for row in results:
				genre3_id = row[0]
				spider.log('Well, here is an gebre3 id : %s.' % genre3_id)
			self.cursor.execute("""INSERT INTO tommymovies_movie_categories (movie_id,category_id) VALUES (%s, %s)""",
					   (new_movie_id, 
					    genre3_id))


		self.conn.commit()


	    except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])


	    return item


