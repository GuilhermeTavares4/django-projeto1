from django.test import TestCase
from django.core import mail

class ContactPostValid(TestCase):

    def setUp(self):
        data = dict(name="Guilherme", email='guideb23@gmail.com',
                    phone='53-12345-6789', message='boa tarde')
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]
    
    
    def test_contact_email_subject(self):
        expect = 'Contato enviado.'
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = 'guideb23@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_contact_email_to(self):
        expect = ['guideb23@gmail.com', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

    def test_contact_Email_body(self):
        contents = (
            'Guilherme',
            'guideb23@gmail.com',
            '53-12345-6789',
            'boa tarde'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)