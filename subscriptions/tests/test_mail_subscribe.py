from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

# Create your tests here.



class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Guilherme', cpf='12345678901', email='guideb23@gmail.com', phone='53 12345-6789')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
    
    
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'guideb23@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_Email_body(self):
        contents = (
            'Guilherme',
            '12345678901',
            'guideb23@gmail.com',
            '53 12345-6789'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)