from django.db import models
from django.contrib import auth
from django.contrib.contenttypes import generic

# our apps
from courses.models import Chunk


class Resource(models.Model):
    """ This is the parent class for the different types of resources.
        The methods of this class need to be overwritten by each subclass
        Note -- this class is ABSTRACT, which means there is no table associated
                with it and therefore a Ressource object does not have an id
                You must get to the actual subclass somehow if you are to maniuplate
                the objects.
    """
    chunk       = generic.GenericRelation(Chunk)

    owner       = models.ForeignKey(auth.models.User)

    created_date= models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


    # METHODS ########################################################
    def __unicode__(self):
        return "resource id:"+str(self.id)
    def render_to_html(self):
        raise NotImplementedError
    def get_edit_form(self):
        raise NotImplementedError




class TextResource(Resource):
    """ This is the CONNECTING TEXT that makes up most part of a lesson
        For now we will assume it is formatted as HTML
    """
    MARKUP_CHOICES = (
        ('text',        'Text'),
        ('html',        'HTML'),
        ('rst',         'reStructuredText'),
        ('dokuwiki',    'DokuWiki syntax'),
        ('mediawiki',   'MediaWiki syntax'),
        #('other',       'Other'),
    )

    markup  = models.CharField(max_length=20, choices=MARKUP_CHOICES, default='html')
    text    = models.TextField()

    # METHODS ########################################################
    def __unicode__(self):
        return self.text[0:80]+"..."
    def render_to_html(self):
        return self.text
    def get_edit_form(self):
        # import statement is here to prevern circular import loop...
        from resources.forms import TextResourceForm
        return TextResourceForm


class LinkResource(Resource):
    """ This is a simple Link resource
    """
    url         = models.URLField()
    title       = models.CharField(max_length=300, help_text="Title", blank=True, null=True)
    caption     = models.CharField(max_length=500, help_text="Caption", blank=True, null=True)
    #is_valid    =

    # METHODS ########################################################
    def __unicode__(self):
        return self.url
    def render_to_html(self):
        # should really be done with a template, but i want a quick somethign something
        # right now
        val='<a href="'+self.url+'">'+self.title+'</a>'
        if self.caption:
            val+='<br/>'
            val+='<p class="caption">'+self.caption+'</p>'
        return val
    def get_edit_form(self):
        from resources.forms import LinkResourceForm
        return LinkResourceForm




