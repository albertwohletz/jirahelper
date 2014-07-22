__author__ = 'albertlwohletz'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^request_access/', 'views.request_access'),
)

