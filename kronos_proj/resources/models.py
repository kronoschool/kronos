from django.db import models
from django.contrib import admin
from django.contrib import auth



class Resource(models.Model):
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





class ResourceAdmin(admin.ModelAdmin):
    """ This is the CourseAdmin class which sets up some niceties for
        use in the django admin ;)  """
    list_display = ('title', 'slug','teacher', 'description', 'created_date')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Resource,ResourceAdmin)

