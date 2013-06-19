# encoding: utf-8
from django.test.testcases import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubcriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
           name='Diego',
           cpf='01234567890',
           email='diego@teste.com',
           phone='62-39201997',
           )
        self.obj.save()
        
    def test_create(self):
        'a inscrição tem que ter os campos'
        self.assertEqual(1, self.obj.id)
        
    def test_as_created_at(self):
        'foi criado automaticamente em'
        self.assertIsInstance(self.obj.created_at, datetime)
        
    def test_cpf_unique(self):
        'cpf unico'
        s=Subscription(
           name='Diego',
           cpf='01234567890',
           email='outro-diego@teste.com',
           phone='62-39201997',
           )
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        'email pode se repetir'
        s=Subscription.objects.create(
           name='Diego',
           cpf='11111111111',
           email='diego@teste.com',
           phone='62-39201997',
           )
        self.assertEqual(2, s.pk)
        
    def test_unicode(self):
        self.assertEqual(u'Diego', unicode(self.obj))
        
    def test_paid_default_value_is_False(self):
        'Por default o campo paid deve ser False'
        self.assertEqual(False, self.obj.paid)    