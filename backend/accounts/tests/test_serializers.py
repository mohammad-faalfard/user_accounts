from common.constants import TestCase
from accounts.api.v1.serializers import LoginSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class TestSerializers(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            user_type="PARENT",
            email="test@example.com",
        )

    def test_login_serializer(self):
        data = {"username": "testuser", "password": "testpassword"}
        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_profile_serializer(self):
        serializer = UserProfileSerializer(instance=self.user)
        self.assertEquals(serializer.data["username"], "testuser")
