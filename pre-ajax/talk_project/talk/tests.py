from django.test import TestCase
from django.core.urlresolvers import resolve


class HomeViewTest(TestCase):

    def test_index(self):
        """Ensure main url is connected to the talk.views.home view"""
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'talk.views.home')
