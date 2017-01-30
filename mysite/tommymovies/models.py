from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils import timezone

class MovieManager(models.Manager):
	def create_movie(self, name, year, watched, watch_date, p_rating, imdb_rating, rt_rating, **categories):
		movie = self.create(name=name,year=year,watched=watched,watch_date=watch_date,p_rating=p_rating,imdb_rating=imdb_rating,rt_rating=rt_rating)
		#movie.categories.add(categories)
		return movie

class Category(models.Model):
	genre = models.CharField(max_length=255, verbose_name="Genre")
	def __str__(self):
		return self.genre
		
class Movie(models.Model):
	name = models.CharField(max_length=50)
	year = models.IntegerField()
	watched = models.BooleanField()
	watch_date = models.DateField('Date_Watched', null=True, blank=True)
	p_rating = models.IntegerField()
	imdb_rating = models.FloatField()
	rt_rating = models.FloatField()
	categories = models.ManyToManyField(Category, blank=True, related_name='movie_categories') 
	def __str__(self):
		return self.name
	objects = MovieManager()




