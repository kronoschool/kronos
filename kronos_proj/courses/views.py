
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context, loader, Template
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse


from models import Lesson, Course, Chunk


#    url(r'^create/$',  'create_course'),
def create_course(request):
    # TODO:
    # to do course landing page with a link to /lesson/create on it
    pass
    


#    url(r'^(?P<course_id>\d+)/lesson/create/$',  'create_lesson'),
def create_lesson(request, course_id):
    """ creates a lesson object and redirects to /edit/ view for that lesson """

    try:
        course=  Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404

    lesson = Lesson(title='',slug='',course=course)
    lesson.save()

    redirect_to = reverse('courses.lessons.views.edit',
                           kwargs={  "course_id":course.id,
                                     "lesson_id":lesson.id,  } ) 

    return HttpResponseRedirect(redirect_to,)


