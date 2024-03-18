from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
