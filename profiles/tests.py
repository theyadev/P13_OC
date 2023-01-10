from django.test import TestCase
from django.urls import reverse

from .models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='Test User', password='Test Password')
        Profile.objects.create(user=user, favorite_city='Test City')

    def test_profile_city(self):
        test_profile = Profile.objects.get(favorite_city='Test City')
        self.assertEqual(test_profile.favorite_city, 'Test City')

    def test_profile_user(self):
        test_profile = Profile.objects.get(user__username='Test User')
        self.assertEqual(test_profile.user.username, 'Test User')

    def test_profile_index_view(self):
        url = reverse('profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test User')

    def test_profile_view(self):
        url = reverse('profile', kwargs={'username': 'Test User'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test City')
