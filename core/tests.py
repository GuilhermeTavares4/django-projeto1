from django.test import TestCase

# Create your tests here.
class HomeTest(TestCase): 

    def setUp(self):
        response = self.client.get('/')
        
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