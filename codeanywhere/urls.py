from django.conf.urls import patterns, include, url
import os.path
from texteditor.views import *
STATIC_ROOT=os.path.join(os.path.dirname(__file__),'templates/static')
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',	
    # Examples:
    url(r'^$',home),
    url(r'^login/$', login),
    url(r'^signin/$', signin),
    url(r'^dashboard/$', dashboard),
    url(r'^subDetails/$', subDetails),
    url(r'^signup/$', Newuser),
    url(r'^new/$', sign_nav),
    url(r'^openTab/$', openTab),
    url(r'^openAjax/$', openAjax),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
    # url(r'^$', 'codeanywhere.views.home', name='home'),
    # url(r'^codeanywhere/', include('codeanywhere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
