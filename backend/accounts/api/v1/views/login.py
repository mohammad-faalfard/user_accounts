from rest_framework_simplejwt.views import TokenObtainPairView
from common.constants import  Response, status
from ..serializers import LoginSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginView(TokenObtainPairView):
    """
    An endpoint to obtain a JWT token for authentication.
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user login.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate tokens
        token = serializer.validated_data
        return Response(token, status=status.HTTP_200_OK)
