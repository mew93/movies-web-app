from .models import Movie, Category
from django.forms import ModelForm, ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div, Field, Column, Row, Button, HTML
from django import forms
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField
from datetime import datetime

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ('name', 'year', 'watched', 'watch_date', 'p_rating', 'imdb_rating', 'rt_rating', 'categories', 'imdb_url', 'rt_url', 'douban_url', 'comment')

	def __init__(self, *args, **kwargs):
		super(MovieForm, self).__init__(*args, **kwargs)
		self.fields['categories'].required = False
		self.fields['watch_date'].required = False
		self.fields['watched'].required = False
	def clean_watch_date(self):
		watch_date = self.cleaned_data['watch_date']
		return watch_date


class MovieTableFormHelper(FormHelper):
	model = Movie
	form_tag = False
	form_class = 'form-inline'
	field_template = 'bootstrap3/layout/inline_field.html'

	layout = Layout(
		Fieldset('Filter',
			Div('name__icontains'),
			Div('year__gte'),
			Div('year__lte'),
			Div('categories__icontains'),
			Div('categories'),
			Div('p_rating__gte'),
			#Div('p_rating__lte'),
			Div('imdb_rating__gte'),
			#Div('imdb_rating__lte'),
			Div('rt_rating__gte'),
			#Div('rt_rating__lte'),
			#Div('id'),
			#Div('id__gte'),
			#Div('id__lte'),
			Div('watch_date__gte'),
			Div('watch_date__lte'),
		)
	)

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ('genre',)
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['genre'] =  ModelChoiceField(queryset=Category.objects.all(), empty_label="Choose a genre",)
		self.fields['genre'].required = False

class NewCategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ('genre',)