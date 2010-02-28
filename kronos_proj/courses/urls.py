from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('courses.views',

    # arriving here after /course
    url(r'^(?P<course_id>\d+)/lesson/(?P<lesson_id>\d+)/',  include('courses.lessons.urls')),

    # creation views
    url(r'^create/$',  'create_course'),
    url(r'^(?P<course_id>\d+)/lesson/create/$',  'create_lesson'),


)


