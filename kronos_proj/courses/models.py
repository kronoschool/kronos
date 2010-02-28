from django.db import models
from django.contrib import auth

# i guess i don't need this -- the apps stay decoupled
#from resources.models import TextResource, LinkResource
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class Course(models.Model):
    """ This is the main folder-like structure that will be available on the site.
        A Course contains Lessonsi
        A course is about a given Topic (not implemented yet)
    """
    title       = models.CharField(max_length=300, help_text="Course title")
    slug        = models.SlugField(max_length=100, help_text="short-title-with-hyphens")
    teacher     = models.ForeignKey(auth.models.User)
    #topic      = model.ForeignKey(topics.Topic)

    #optional fields
    description  = models.TextField(max_length=500, help_text="describe the course in 3 sentences.")
    # why not?
    image       = models.ImageField(  blank=True, upload_to="uploads/course_images/")

    created_date = models.DateField(auto_now_add=True)
    edited_date  = models.DateField(auto_now=True)

    def __unicode__(self):
       return self.title   # return title as string version of obj



class Lesson(models.Model):
    """ This is the main unit of content that will be distributed according to a schedule
        A lesson is part of a Course
        A lesson consists of many Chunks

        A lesson is associated with a User (student role) via a Schedule

    """
    title       = models.CharField(max_length=300, help_text="Lesson title")
    slug        = models.SlugField(max_length=100, help_text="short-title-with-hyphens")
    course      = models.ForeignKey(Course)
    #topic      = model.ForeignKey(topics.Topic)

    #optional fields
    description  = models.TextField(max_length=500, help_text="What is this lesson about (in 3 sentences).", blank=True)

    created_date = models.DateField(auto_now_add=True)
    edited_date  = models.DateField(auto_now=True)

    def __unicode__(self):
       return self.title   # return title as string version of obj








class Chunk(models.Model):
    """ The Chunks are basic building blocks of Lessons
        Each Chunk points to a Resource

    """
    lesson      = models.ForeignKey(Lesson)
    order       = models.IntegerField()

    res_type    = models.ForeignKey(ContentType)
    res_id      = models.PositiveIntegerField()
    resource    = generic.GenericForeignKey('res_type', 'res_id')


    def __unicode__(self):
       return self.lesson.title+" order:"+str(self.order)  #+" --> resource:"+str(resource.id)



