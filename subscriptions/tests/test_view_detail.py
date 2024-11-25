from django.test import TestCase
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r

class SubscriptionDetailGet(TestCase):
    def setUp(self):
        obj = Subscription.objects.create(
            name='Guilherme',
            cpf='12345678901',
            email='guideb23@gmail.com',
            phone='53-12345-6789'
        )
        self.resp = self.client.get(r('subscriptions:detail', obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Guilherme', '12345678901',
                    'guideb23@gmail.com', '53-12345-6789')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(resp.status_code, 404)