from django.forms import Form, ModelForm, ModelChoiceField, MultipleChoiceField
from django import forms

from resources.models import TextResource, LinkResource


class TextResourceForm(ModelForm):
    """ This is the edit-form for creating a TextResource """
    class Meta:
        model = TextResource


class LinkResourceForm(ModelForm):
    """ This is the edit-form for creating a TextResource """
    class Meta:
        model = LinkResource


