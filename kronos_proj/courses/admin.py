from django.contrib import admin
from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    """ This is the CourseAdmin class which sets up some niceties for
        use in the django admin ;)  """
    list_display = ('title', 'slug','teacher', 'description', 'created_date')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Course,CourseAdmin)


class LessonAdmin(admin.ModelAdmin):
    """ This is the CourseAdmin class which sets up some niceties for
        use in the django admin ;)  """
    list_display = ('title', 'slug','course', 'description', 'created_date')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Lesson,LessonAdmin)




class ChunkAdmin(admin.ModelAdmin):
    """ This is the CourseAdmin class which sets up some niceties for
        use in the django admin ;)  """
        pass

admin.site.register(Chunk,ChunkAdmin)

