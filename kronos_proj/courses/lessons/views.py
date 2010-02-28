from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, Context, loader, Template
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse



from courses.models import Lesson, Course, Chunk


# views that handle lesson actions

#    # base views
#    url(r'^$',                         'display'),
#    url(r'^edit/$',                    'edit'),

def display(request,course_id,lesson_id):
    pass

def edit(request,course_id,lesson_id):
    """ BASE chunker edit view 
        most of the rendering is done on the client side after page loads"""

    try:
        course=  Course.objects.get(pk=course_id)
        lesson=  Lesson.objects.get(pk=lesson_id)
    except (Course.DoesNotExist, Lesson.DoesNotExist):
        raise Http404

    number_of_chunks= Chunk.objects.filter(lesson=lesson).count();

    t = loader.get_template('chunker.html')
    c = RequestContext(request, {   'course_id': course_id,
                                    'lesson_id': lesson_id,
                                    'number_of_chunks': number_of_chunks,
            }) 
    # extra parameter number_of_chunks
    # upon loading js needs to:
    #   1/ call get_meta to display title / descrip
    #   2/ loop i from 0 to number_of_chunks calling
    #      /course/1/lesson/123/ajax/render_html/?order=i
    return HttpResponse(t.render(c))


#    # lesson API
#    url(r'^ajax/get_meta/$',      'get_meta'),
def get_meta(request,course_id,lesson_id):
    pass


#    url(r'^ajax/post_meta/$',     'post_meta'),
def post_meta(request,course_id,lesson_id):
    pass


#    url(r'^ajax/insert_chunk/$',  'insert_chunk'),
def insert_chunk(request,course_id,lesson_id):
    pass


#    url(r'^ajax/update_chunk/$',  'insert_chunk'),
def update_chunk(request,course_id,lesson_id):
    pass


#    url(r'^ajax/delete_chunk/$',  'delete_chunk'),
def delete_chunk(request,course_id,lesson_id):
    pass


#    # proxy views for the appropriate ressource methods
#    # a.k.a Ressource API
#    url(r'^ajax/edit_form/$',     'edit_form'),
def edit_form(request,course_id,lesson_id):
    """ returns an edit form suitable for the chunk identified by 
        'order' in the lesson 
        REQUIRED GET PARAMS: order       """
    pass


#    url(r'^ajax/render_html/$',   'render_html'),
def render_html(request,course_id,lesson_id):
    """ returns the html rendered version of chunk which is
        is at location 'order' in the lesson
        REQUIRED GET PARAMS: order       """
    pass


#    url(r'^ajax/render_json/$',   'render_json'),
def render_json(request,course_id,lesson_id):
    """ returns a json representation  for the chunk identified
        at location 'order' in the lesson
        REQUIRED GET PARAMS: order      

        the fields of the json dict depend on what type of chunk it is
        but always match the fields in edit_form  """
        
    pass




