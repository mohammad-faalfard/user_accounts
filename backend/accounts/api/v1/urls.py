# posts/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import (
    LoginView,
    UserProfileRetrieveAPIView,
    UserProfileUpdateAPIView,
)


app_name = "accounts"
urlpatterns = [
    # a mechanism for clients to obtain a token given the username/password.
    path("login/", LoginView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "<uuid:pk>/profile/",
        UserProfileRetrieveAPIView.as_view(),
        name="user-profile-retrieve",
    ),
    path(
        "<uuid:pk>/profile/update/",
        UserProfileUpdateAPIView.as_view(),
        name="user-profile-update",
    ),
]
