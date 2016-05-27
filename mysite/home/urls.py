from django.conf import settings
from django.conf.urls import patterns, url, static

from . import views

urlpatterns = patterns('',
    url(r'search', views.search, name='search'),
    # url(r'^(?P<search>.*)', views.search, name='search'),
    # url(r'^.*search=.*', views.search2, name='search2'),
    url(r'^$', views.index, name='index'),
)