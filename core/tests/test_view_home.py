from django.test import TestCase
from django.shortcuts import resolve_url as r

# Create your tests here.
class HomeTest(TestCase): 

    def setUp(self):
        self.response = self.client.get(r('home'))
        
    def test_get(self):
        '''
        Testa se retorna status code 200
        '''
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        '''
        Testa se está usando o arquivo index.html
        '''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_link_subscription(self):
        self.assertContains(self.response, 'href="{}"'.format(r('subscriptions:new')))