from common.constants import generics, User
from common.permissions import permissions, IsOwnerOrReadOnly

from ..serializers import UserProfileSerializer


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
