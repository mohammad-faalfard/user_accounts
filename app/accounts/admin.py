from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the User model.

    This class defines how the User model will be displayed and managed
    in the Django admin interface.
    """

    # List display fields in the admin interface
    list_display = ("username", "user_type", "is_active", "is_staff", "is_superuser")

    # Filter options in the admin interface
    list_filter = ("user_type", "is_active", "is_staff", "is_superuser")

    # Search fields in the admin interface
    search_fields = ("username", "first_name", "last_name", "email")

    # Fields to display in detail view
    fieldsets = (
        (None, {"fields": ("username", "user_type", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "date_of_birth",
                    "address",
                    "phone_number",
                    "website",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Additional Info", {"fields": ("bio", "profile_picture")}),
    )

    # Define readonly fields
    readonly_fields = ("last_login",)

    # Auto-generated fields
    readonly_fields += ("id", "last_login")

    # Prepopulated fields
    prepopulated_fields = {"username": ("first_name", "last_name")}

    # Custom actions
    actions = ["make_staff", "make_superuser"]

    def make_staff(self, request, queryset):
        """
        Custom action to mark selected users as staff.
        """
        queryset.update(is_staff=True)

    make_staff.short_description = "Mark selected users as staff"

    def make_superuser(self, request, queryset):
        """
        Custom action to mark selected users as superusers.
        """
        queryset.update(is_staff=True, is_superuser=True)

    make_superuser.short_description = "Mark selected users as superusers"


# Register the User model and UserAdmin configuration with the admin site
admin.site.register(User, UserAdmin)
