# encoding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'o form tem que ter os campos'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF somente digitos'
        form = self.make_validated_form(cpf='abc00000000')
        self.assertItemsEqual(['cpf'], form.errors)
    
    def test_cpf_has_11_digits(self):
        'CPF deve ter 11 digitos'
        form = self.make_validated_form(cpf='123')
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_email_is_optional(self):
        'email opcional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
        
    def make_validated_form(self, **kwargs):
        data = dict(name='Diego Tolentino', email='diegotolentino@gmail.com',
                    cpf='12345678901', phone='62-39201997')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
        
