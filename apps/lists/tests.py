from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page


class HomePageTest(TestCase):

    def test_get_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
