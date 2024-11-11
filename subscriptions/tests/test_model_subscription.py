from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name = 'Guilherme',
            cpf = '12345678901',
            email = 'guideb23@gmail.com',
            phone = '53-12345-6789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Guilherme', str(self.obj))

    