# encoding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
           name='Diego',
           cpf='111111111112',  # cpf invalido
           email='diego@teste.com',
           phone='62-39201997',
           )
        self.resp = self.client.get('/inscricao/%s/' % s.pk);

    def test_get(self):
        'se o /inscricao/1/ retorna status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'usa o template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context tem que ter uma instancia de Subscription'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp, 'Diego')

class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/1/')
        self.assertEqual(404, response.status_code)
