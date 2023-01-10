from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):
    def test_index_view(self):
        url = reverse('index')
        profile_url = reverse('profiles_index')
        letting_url = reverse('lettings_index')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, profile_url)
        self.assertContains(response, letting_url)
