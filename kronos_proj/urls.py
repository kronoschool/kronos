from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^kronos_proj/', include('kronos_proj.foo.urls')),

    url(r'^chunker/$', direct_to_template, {'template': 'chunker.html'}, name='chunker'),
    url(r'^etherpad/$', direct_to_template, {'template': 'etherpad/index.html'}, name='etherpad'),
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='home'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


# local_urls.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_urls import *
except ImportError, e:
    print "Error importing local urls:"
    print e

