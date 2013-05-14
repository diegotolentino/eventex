# encoding: utf-8

from django.core.urlresolvers import reverse as r
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'testando se o status code da resposta é o correto'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'testando se o template é o correto'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'testando o html retornado'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'o html tem que ter o token csrf de segurança'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'o contexto tem que ter um form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
           name='Diego',
           cpf='11111111111',
           email='diego@teste.com',
           phone='62-39201997',
           )
        self.resp = self.client.post(r('subscriptions:subscribe'), data);

    def test_post(self):
        'testando se o post redireciona p/ /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'se o post realmente salvou algo'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
           name='Diego',
           cpf='111111111112',  # cpf invalido
           email='diego@teste.com',
           phone='62-39201997',
           )
        self.resp = self.client.post(r('subscriptions:subscribe'), data);

    def test_post(self):
        'testando se o post não redireciona p/ "/inscricao/1/" e sim p/ "/inscricao/"'
        self.assertEqual(200, self.resp.status_code)

    def test_form_erros(self):
        'se o form contem erros'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Não salvou dados'
        self.assertFalse(Subscription.objects.exists())
