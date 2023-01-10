from django.test import TestCase
from django.urls import reverse

from .models import Letting
from .models import Address


class LettingTestCase(TestCase):
    def setUp(self):
        address = Address.objects.create(
            street='Test Street', city='Test City', state='Test State', zip_code=88901, number=12)
        Letting.objects.create(title='Test Letting', address=address)

    def test_letting_title(self):
        test_letting = Letting.objects.get(title='Test Letting')
        self.assertEqual(test_letting.title, 'Test Letting')

    def test_letting_address(self):
        test_letting = Letting.objects.get(address__street='Test Street')
        self.assertEqual(test_letting.address.city, 'Test City')

    def test_letting_index_view(self):
        url = reverse('lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')

    def test_letting_view(self):
        url = reverse('letting', kwargs={'letting_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, 'Test Street')
