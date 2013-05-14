# encoding: utf-8

from django.core.urlresolvers import reverse as r
from django.test import TestCase

class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:homepage'))
        
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
