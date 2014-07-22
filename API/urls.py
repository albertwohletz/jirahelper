__author__ = 'albertlwohletz'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^request_access/', 'API.views.request_access'),
    url(r'^approve_request/', 'API.views.approve_request'),
    url(r'^remove_request/', 'API.views.remove_request'),
)

