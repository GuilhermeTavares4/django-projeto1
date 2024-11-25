from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail

class ContactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'contact/contact_form.html')
        
    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 5),
            ('type="text"', 2),
            ('<textarea', 1),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Guilherme", email='guideb23@gmail.com',
                    phone='53-12345-6789', message='boa tarde')
        self.resp = self.client.post('/contato/', data)

    def test_post(self):
        self.assertRedirects(self.resp, '/contato/')

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))

class ContactPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contato/')

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)




    

