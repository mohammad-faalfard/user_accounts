"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from common.permissions import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include


# Define the schema view for Swagger documentation
schema_view = get_schema_view(
    # Define basic information about the API
    openapi.Info(
        title="xyz API",  # Title of the API
        default_version="1.0.0",  # Default version of the API
        description="Welcome to xyz school",  # Description of the API
        terms_of_service="https://policies.google.com/terms?hl=en-US",  # Terms of service (if any)
        contact=openapi.Contact(
            email="example@example.com"
        ),  # Contact information for the API
        license=openapi.License(name="xyz School"),  # License information for the API
    ),
    # Set the schema view to be public
    public=True,
    # Set permissions for accessing the schema view (only admin users)
    permission_classes=(permissions.IsAdminUser,),
)


urlpatterns = [
    path("admin/", admin.site.urls),  # URL for Django admin interface
    # Swagger documentation URLs
    path(
        "swagger<str:format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),  # URL for raw OpenAPI schema in JSON or YAML format
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),  # URL for Swagger UI to interactively explore API documentation
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),  # URL for ReDoc UI as an alternative to Swagger UI for API documentation
    path(
        "api/v1/accounts/",
        include(
            "accounts.api.v1.urls",
            namespace="v1_accounts",
        ),  # URL for accounts API version 1, including its endpoints
    ),
]
