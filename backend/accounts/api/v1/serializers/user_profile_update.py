from common.constants import serializers, User


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
