from django.conf.urls import url

from . import views

app_name = 'tommymovies'
urlpatterns = [
	url(r'^$', views.WatchHistoryView.as_view(), name='history'),
	#url(r'^/saved/$', views.ToWatchListView.as_view(), name='saved'),
	url(r'^add/$', views.add, name = 'add'),
	url(r'^delete/(?P<movie_id>\d+)/$', views.delete, name = 'delete'),
	url(r'^watched/(?P<movie_id>\d+)/$', views.toggle_watched, name = 'toggle_watched'),
	url(r'^movie/(?P<movie_id>\d+)/$', views.MovieDetailView.as_view(), name='movie'),
	url(r'^movie/edit/(?P<movie_id>\d+)/$', views.MovieEditView.as_view(), name='edit'),
	url(r'^movie/edit/(?P<movie_id>\d+)/submit$', views.edit_submit, name = 'edit_submit'),
	#url(r'^history/table/$', views.table_movie_history, name = 'table_movie_history'),
	#url(r'^saved/table/$', views.table_to_watch, name = 'table_to_watch'),
	url(r'^history/table/$', views.MovieTableView.as_view(title='Movie Watch History', watched = 1), name = 'movie_history_table'),
	url(r'^saved/table/$', views.MovieTableView.as_view(title='Movies to Watch', watched = 0), name = 'to_watch_table'),
	url(r'^category/add$', views.addCategory, name = 'addCategory'),
	url(r'^categorize/$', views.categorize_form, name = 'categorize'),
	url(r'^categorize/submit$', views.categorize, name = 'categorize_submit'),
	url(r'^movie/add$', views.addMovie, name = 'addMovie'),
	url(r'^movie/add/submit$', views.addMovieSubmit, name = 'addMovieSubmit'),
	url(r'^url/$', views.addByUrl_form, name = 'addByUrl_form'),
	url(r'^url/submit$', views.addByUrl_submit, name = 'addByUrl_submit'),

]
