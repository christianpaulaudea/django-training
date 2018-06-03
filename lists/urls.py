from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^books/$', views.books, name='books'),
	url(r'^books/new/$', views.new_book, name='new_book'),
	url(r'^books/(?P<pk>\d+)/edit/$', views.edit_book, name='edit_book'),
	url(r'^books/(?P<pk>\d+)/delete/$', views.delete_book, name='delete_book'),

	url(r'^movies/$', views.movies, name='movies'),
	url(r'^movies/new/$', views.new_movie, name='new_movie'),
	url(r'^movies/(?P<pk>\d+)/edit/$', views.edit_movie, name='edit_movie'),
	url(r'^movies/(?P<pk>\d+)/delete/$', views.delete_movie, name='delete_movie'),

	url(r'^holidays/$', views.holidays, name='holidays'),
	url(r'^holidays/new/$', views.new_holiday, name='new_holiday'),
	url(r'^holidays/(?P<pk>\d+)/edit/$', views.edit_holiday, name='edit_holiday'),
	url(r'^holidays/(?P<pk>\d+)/delete/$', views.delete_holiday, name='delete_holiday'),
]
