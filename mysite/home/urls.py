from django.conf import settings
from django.conf.urls import patterns, url, static

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)