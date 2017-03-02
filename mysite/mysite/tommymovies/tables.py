import django_tables2 as tables
from .models import Movie
from django.urls import reverse
from django.conf.urls import url
import views

class MovieTable(tables.Table):
	imdb_url = tables.TemplateColumn('<a href={{ record.imdb_url }} target="_blank">IMDB</a>', orderable=False,  empty_values=(),verbose_name= 'IMDB')
	rt_url = tables.TemplateColumn('<a href={{ record.rt_url }} target="_blank">RT</a>', orderable=False, empty_values=(),verbose_name= 'RT')
	douban_url = tables.TemplateColumn('<a href={{ record.douban_url }} target="_blank">Douban</a>', orderable=False, empty_values=(),verbose_name= 'Douban')
	edit = tables.TemplateColumn('<a href="{% url \'tommymovies:edit\' record.id %}">+</a>', orderable=False, empty_values=())
	delete = tables.TemplateColumn('<a href="{% url \'tommymovies:delete\' record.id %}">-</a>', orderable=False, empty_values=())
	toggle_watched  = tables.TemplateColumn('<a href="{% url \'tommymovies:toggle_watched\' record.id %}">x</a>', orderable=False, empty_values=())
	name = tables.TemplateColumn('<a href="{% url \'tommymovies:movie\' record.id %}">{{record.name}}</a>', empty_values=(), verbose_name= 'Movie')
	year = tables.Column(verbose_name= 'Year' )
	watched = tables.Column(verbose_name= 'Watched?' )
	watch_date = tables.Column(verbose_name= 'Date Watched' )
	p_rating = tables.Column(verbose_name= 'Personal Rating' )
	imdb_rating = tables.TemplateColumn('<a href={{ record.imdb_url }} target="_blank">{{record.imdb_rating}}</a>', empty_values=(),verbose_name= 'IMDB')
	rt_rating = tables.TemplateColumn('<a href={{ record.rt_url }} target="_blank">{{record.rt_rating}}</a>', empty_values=(),verbose_name= 'RT')
	categories = tables.Column(verbose_name= 'Genre')


	class Meta:
		model = Movie
		attrs = {'class': 'paleblue'}
		exclude = ('imdb_url','rt_url', 'douban_url', 'comment')
		sequence = ('id', 'name', 'year', 'p_rating', 'imdb_rating', 'rt_rating', 'categories', 'watched', 'watch_date', 'edit', 'delete', 'toggle_watched')
	def render_categories(self, record):
		if record.categories is not None:
			return ', '.join([categories.genre for categories in record.categories.all()])
		return '-'

