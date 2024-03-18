from common.constants import generics, MultiPartParser, FormParser, User
from common.permissions import permissions, IsOwnerOrReadOnly

from ..serializers import UserProfileUpdateSerializer


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
