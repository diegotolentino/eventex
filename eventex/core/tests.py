# encoding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#from django.http import response
# from gunicorn.http.wsgi import Response


class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        
    def test_get(self):
        'Get / tem que retornar code_200'
        self.assertEqual(200, self.resp.status_code)
        
    def test_template(self):
        'Tem que devolver o template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
        
        
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
