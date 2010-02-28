from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('courses.lessons.views',

    # arriving here after /course/(?P<course_id>\d+)/lesson/(?P<lesson_id>\d+)/

    # base views
    url(r'^$',                         'display'),
    url(r'^edit/$',                    'edit'),

    # lesson API
    url(r'^ajax/get_meta/$',      'get_meta'),
    url(r'^ajax/post_meta/$',     'post_meta'),
    url(r'^ajax/update_chunk/$',  'insert_chunk'),
    url(r'^ajax/insert_chunk/$',  'insert_chunk'),
    url(r'^ajax/delete_chunk/$',  'delete_chunk'),
    
    # proxy views for the appropriate ressource methods
    # a.k.a Ressource API
    url(r'^ajax/edit_form/$',     'edit_form'),
    url(r'^ajax/render_html/$',   'render_html'),       #get_chunk
    url(r'^ajax/render_json/$',   'render_json'),

)


