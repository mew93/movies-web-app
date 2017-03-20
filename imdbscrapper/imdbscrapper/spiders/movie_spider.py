import scrapy
from scrapy.loader import ItemLoader
from imdbscrapper.items import MovieItem
from six import string_types

class MovieSpider(scrapy.Spider):
	name = "movie"
	def __init__(self, *args, **kwargs): 
		super(MovieSpider, self).__init__(*args, **kwargs) 
		self.start_urls = [kwargs.get('start_url')] 
		

	def parse(self, response):
		genres = []
		item = MovieItem()
		for movie in response.css('div.title_bar_wrapper'):
			item['name'] = movie.css('div.title_wrapper h1::text').extract_first()
			item['year'] = movie.css('div.title_wrapper span a::text').extract_first()
			item['imdb_rating'] = movie.css('div.ratingValue strong span::text').extract()
			item['duration'] = movie.css('div.subtext time::text').extract()
			for genre in response.css('div.subtext a'):
				print(genre.css('span.itemprop::text').extract_first())
				#item['genre'] = genre.css('span.itemprop::text').extract_first()
				genres.append(genre.css('span.itemprop::text').extract_first())
			item['genre1'] = genres[0]
			item['genre2'] = genres[1]
			item['genre3'] = genres[2]
			item['imdb_url'] = response.url

			item['name'] = item['name'].replace(u'\xa0', u' ')
			search_url = 'http://www.bing.com/search?q=rotten+tomatoes+' + item['name']
			proper_string = isinstance(search_url, string_types)
			self.logger.info('Logged: search_url proper_string %s', proper_string)

			if search_url is not None:
				return scrapy.Request(search_url, callback=self.parse_search, meta={'item': item})
	

	def parse_search(self, response):
		item = response.meta['item']
		rt_url = response.css('li.b_algo h2 a::attr(href)').extract_first()
		self.logger.info('Logged rt_url %s', rt_url)
		if rt_url is not None:
			return scrapy.Request(rt_url, callback=self.parse_rt, meta={'item': item})

	def parse_rt(self, response):
		item = response.meta['item']
		item['rt_url'] = response.url
		item['rt_critic_rating'] = critic_rating = response.css('div.critic-score.meter span.meter-value.superPageFontColor span::text').extract_first()
		item['rt_audience_rating'] = audience_rating = response.css('div.audience-score.meter div.meter-value span.superPageFontColor::text').extract_first()
		return item



