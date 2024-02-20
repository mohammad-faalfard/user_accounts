from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import (
    LoginView,
    UserProfileRetrieveAPIView,
    UserProfileUpdateAPIView,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class TestUrls(TestCase):
    """
    Test class for URL resolution in the accounts app.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            user_type="PARENT",
            email="test@example.com",
        )

    def test_login_url_resolves(self):
        """
        Test that the login URL resolves to the LoginView.
        """
        url = reverse("accounts:token_obtain_pair")
        # Verify that the resolved view class is LoginView
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_profile_retrieve_url_resolves(self):
        """
        Test that the profile retrieve URL resolves to the UserProfileRetrieveAPIView.
        """
        url = reverse("accounts:user-profile-retrieve", args=[self.user.pk])
        # Verify that the resolved view class is UserProfileRetrieveAPIView
        self.assertEquals(resolve(url).func.view_class, UserProfileRetrieveAPIView)

    def test_profile_update_url_resolves(self):
        """
        Test that the profile update URL resolves to the UserProfileUpdateAPIView.
        """
        url = reverse("accounts:user-profile-update", args=[self.user.pk])
        # Verify that the resolved view class is UserProfileUpdateAPIView
        self.assertEquals(resolve(url).func.view_class, UserProfileUpdateAPIView)

