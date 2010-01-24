"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from resources.models import TextResource
from django.contrib import auth



class SimpleTest(TestCase):
    def test_basic_TextResource(self):
        """
        Creates a TextResource and checks if it has the right text
        """
        dummy = auth.models.User(username="john")
        dummy.save()

        s = "alskj aslkj "
        t = TextResource(text=s, owner=dummy)
        t.save()

        self.failUnlessEqual(t.text, s)
        self.failUnlessEqual(t.owner.id, dummy.id)

