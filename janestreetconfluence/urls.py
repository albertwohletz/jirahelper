from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Confluence API.  Currently just a local database, this component would change when advancing from prototype to
    # real implementation.
    url(r'^api/', include('API.urls')),

    # Default Page
    url(r'^$', 'Interface.views.default'),


    url(r'^request/(?P<space_name>\S+)/$', 'Interface.views.request_access'),
    url(r'^request/default', 'Interface.views.request_page'),
    url(r'^manage/', 'Interface.views.manage'),
    # Django Admin Tools
    url(r'^admin/', include(admin.site.urls)),
)
