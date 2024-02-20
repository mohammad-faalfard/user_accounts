from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    LoginSerializer,
    UserProfileSerializer,
    UserProfileUpdateSerializer,
)
from .permissions import IsOwnerOrReadOnly


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


class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
    """
    A view for retrieving user profile.
    """

    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        """
        Retrieve the queryset of the current authenticated user only.
        """
        return User.objects.filter(id=self.request.user.id)


class UserProfileUpdateAPIView(generics.UpdateAPIView):
    """
    A view for updating user profile.
    """

    serializer_class = UserProfileUpdateSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        """
        Retrieve the queryset of the current authenticated user only.
        """
        return User.objects.filter(id=self.request.user.id)

