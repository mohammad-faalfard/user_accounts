from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import  APIClient
from rest_framework import status


User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        # Create a test client and request factory
        self.client = APIClient()
        self.factory = RequestFactory()

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            user_type='PARENT',
            email='test@example.com'
        )

        # Authenticate the test client with the test user
        self.client.force_authenticate(user=self.user)

    def test_login_view(self):
        # Test the LoginView by making a POST request to the login URL
        url = reverse('accounts:token_obtain_pair')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_profile_retrieve_view(self):
        # Test the UserProfileRetrieveAPIView by making a GET request to the profile retrieve URL
        url = reverse('accounts:user-profile-retrieve', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_profile_update_view(self):
        # Test the UserProfileUpdateAPIView by making a PUT request to the profile update URL
        url = reverse('accounts:user-profile-update', kwargs={'pk': self.user.pk})
        data = {'bio': 'Updated biography'}  # Example data for updating the profile
        response = self.client.put(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

 
