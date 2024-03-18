import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError, PermissionDenied
from django.core.validators import validate_email

from .managers import UserManager
from ..validators import validate_national_id


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the application.

    Attributes:
        id (UUIDField): Unique identifier for the user.
        user_type (CharField): Type of user (e.g., parent, teacher, etc.).
        username (CharField): National ID of the user.
        is_active (BooleanField): User's active status.
        is_staff (BooleanField): User's staff status.
        is_superuser (BooleanField): User's superuser status.
        last_login (DateField): Date of last login.
        bio (TextField): User's biography.
        profile_picture (ImageField): User's profile picture.
        first_name (CharField): User's first name.
        last_name (CharField): User's last name.
        email (EmailField): User's email address.
        date_of_birth (DateField): User's date of birth.
        address (CharField): User's address.
        phone_number (CharField): User's phone number.
        website (URLField): User's website URL.
    """

    class Meta:
        app_label = "accounts"
        verbose_name = "User"
        verbose_name_plural = "Users"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Type(models.TextChoices):
        PARENT = "PARENT", "Parent"
        TEACHER = "TEACHER", "Teacher"
        DRIVER = "DRIVER", "Driver"
        DEPUTY = "DEPUTY", "Deputy Admin"
        SERVICE = "SERVICE", "Service Admin"
        LIBRARY = "LIBRARY", "Library Admin"
        BUFFET = "BUFFET", "Buffet Admin"
        MANAGER = "MANAGER", "School Manager"

    user_type = models.CharField(
        verbose_name="User Type",
        help_text="Choose user type from Parent, Teacher, Driver, Deputy Admin, Service Admin, Library Admin",
        choices=Type.choices,
        max_length=20,
        blank=False,
    )

    username = models.CharField(
        verbose_name="National ID",
        max_length=10,
        unique=True,
        help_text=("Ten digits"),
        validators=[validate_national_id],
    )

    is_active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="Admin",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="School Manager",
        default=False,
    )

    last_login = models.DateField(
        verbose_name="Last Login",
        blank=True,
        null=True,
    )

    # Profile fields
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        verbose_name="Profile Picture",
    )

    # Personal information
    first_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Last Name"
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        null=True,
        verbose_name="Email",
        validators=[validate_email],
    )

    # Additional fields
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Date of Birth"
    )
    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Address"
    )
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Phone Number"
    )
    website = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Website"
    )

    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self) -> str:
        """Return a string representation of this `User`."""
        return self.username

    def get_short_name(self) -> str:
        """Return user username."""
        return self.username

    def save(self, *args, **kwargs):
        """
        Save the user instance.

        Set is_staff to True for different admin groups.
        """
        admin_groups = [
            self.Type.SERVICE,
            self.Type.DEPUTY,
            self.Type.LIBRARY,
            self.Type.BUFFET,
            self.Type.MANAGER,
        ]
        if self.user_type in admin_groups:
            self.is_staff = True
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        """
        Delete the user instance.

        Raise PermissionDenied if attempting to delete a School Manager user.
        """
        if self.user_type == self.Type.MANAGER:
            raise PermissionDenied("Deleting a School Manager user is not allowed.")
        super().delete(using, keep_parents)

    def clean(self):
        """
        Clean method for validating user instance.

        Check if there is already a school manager user and raise ValidationError if so.
        """
        super().clean()
        if (
            self.user_type == self.Type.MANAGER
            and User.objects.filter(user_type=self.Type.MANAGER).exists()
        ):
            raise ValidationError("Only one School Manager user is allowed.")
