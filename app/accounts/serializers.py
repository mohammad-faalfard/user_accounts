from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class LoginSerializer(TokenObtainPairSerializer):
    """
    Serializer for user login, based on TokenObtainPairSerializer.
    
    This serializer is used for authenticating users and generating JWT tokens.
    """

    def validate(self, attrs):
        """
        Validate user credentials and generate JWT tokens.

        Args:
            attrs (dict): Dictionary containing user credentials.

        Returns:
            dict: A dictionary containing JWT tokens along with user information.
        """
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        data["user_type"] = self.user.user_type
        data["id"] = self.user.id
        data["is_active"] = self.user.is_active
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile information.

    This serializer is used for serializing user profile data.
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "user_type",
            "bio",
            "profile_picture",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "address",
            "phone_number",
            "website",
        )
        read_only_fields = ("id", "username", "user_type")


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user profile information.

    This serializer is used for updating user profile data.
    """

    class Meta:
        model = User
        fields = (
            "bio",
            "profile_picture",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "address",
            "phone_number",
            "website",
        )
