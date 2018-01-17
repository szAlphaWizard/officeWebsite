#! -*- coding:utf8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'web.views.index'),
)