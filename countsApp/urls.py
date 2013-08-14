from django.conf.urls import patterns, url

from countsApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)