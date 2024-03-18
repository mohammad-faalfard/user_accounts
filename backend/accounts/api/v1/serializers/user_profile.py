from common.constants import serializers, User


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
