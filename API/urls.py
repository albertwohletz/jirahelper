__author__ = 'albertlwohletz'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^addaccess/', 'Interface.views.request_page'),

)

