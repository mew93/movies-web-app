import scrapy
from items import MovieItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    def __init__(self, *args, **kwargs): 
		super(MovieSpider, self).__init__(*args, **kwargs) 

		self.start_urls = [kwargs.get('start_url')] 

    def parse(self, response):
        for movie in response.css('div.title_bar_wrapper'):
			yield {
				'title': movie.css('div.title_wrapper h1::text').extract_first(),
				'year': movie.css('div.title_wrapper span a::text').extract_first(),
				'rating': movie.css('div.ratingValue strong span::text').extract(),
				'duration': movie.css('div.subtext time::text').extract()
			}
			for genre in response.css('div.subtext a'):
				yield {
					'genre': genre.css('span.itemprop::text').extract_first()
				}


