from django.conf.urls import patterns, url

from api import views 

urlpatterns = patterns('',
  url(r'^words/$', views.index_words, name='words'),
  url(r'^appearances/$', views.index_appearances, name='appearances'),
  url(r'^listings/$', views.index_listings, name='listings')
)
