from django.contrib import admin
#from resources.models import Resource
from resources.models import TextResource, LinkResource


# Since it is an abstract class it does not get its own admin!
#class ResourceAdmin(admin.ModelAdmin):
# NONE


class TextResourceAdmin(admin.ModelAdmin):
    """ An admin for a text resource
    """
    pass

admin.site.register(TextResource,TextResourceAdmin)

class LinkResourceAdmin(admin.ModelAdmin):
    """ An admin for a link resource
    """
    pass

admin.site.register(LinkResource,LinkResourceAdmin)
