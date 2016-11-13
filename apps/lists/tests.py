from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from .views import home_page


class HomePageTest(TestCase):

    def test_get_home_page(self):
        """Check if / is home_page view"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_contains(self):
        """Check if / have title tag"""
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_template(self):
        """Check if / use index.html"""
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
