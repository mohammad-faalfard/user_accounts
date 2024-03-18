from common.constants import PermissionDenied, TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTests(TestCase):
    """
    Test cases for the custom User model.
    """

    def setUp(self):
        """
        Set up method to instantiate the custom User model.
        """
        self.User = User

    def test_create_user(self):
        """
        Test creating a regular user.
        """
        user = self.User.objects.create_user(
            username="1234567890", user_type=User.Type.PARENT
        )
        # Check if the user attributes are set correctly
        self.assertEqual(user.username, "1234567890")
        self.assertEqual(user.user_type, User.Type.PARENT)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Test creating a superuser.
        """
        superuser = self.User.objects.create_superuser(
            username="1234567890", user_type=User.Type.MANAGER
        )
        # Check if the superuser attributes are set correctly
        self.assertEqual(superuser.username, "1234567890")
        self.assertEqual(superuser.user_type, User.Type.MANAGER)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_without_staff_permission(self):
        """
        Test creating a superuser without staff permission (which is not allowed).
        """
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                username="1234567890", user_type=User.Type.MANAGER, is_staff=False
            )

    def test_create_superuser_without_superuser_permission(self):
        """
        Test creating a superuser without superuser permission (which is not allowed).
        """
        with self.assertRaises(ValueError):
            self.User.objects.create_superuser(
                username="1234567890", user_type=User.Type.MANAGER, is_superuser=False
            )

    def test_delete_user(self):
        """
        Test deleting a regular user.
        """
        user = self.User.objects.create_user(
            username="1234567890", user_type=User.Type.PARENT
        )
        # Check if the user is deleted successfully
        user.delete()
        self.assertFalse(self.User.objects.filter(username="1234567890").exists())

    def test_delete_manager_user(self):
        """
        Test deleting a manager user (which should raise PermissionDenied).
        """
        manager_user = self.User.objects.create_user(
            username="9876543210", user_type=User.Type.MANAGER
        )
        with self.assertRaises(PermissionDenied):
            manager_user.delete()

    def test_save_method_set_staff(self):
        """
        Test saving a user with a user type that should have staff permissions.
        """
        admin_user = self.User.objects.create_user(
            username="9876543210", user_type=User.Type.SERVICE
        )
        self.assertTrue(admin_user.is_staff)

    def test_save_method_not_set_staff(self):
        """
        Test saving a regular user without staff permissions.
        """
        regular_user = self.User.objects.create_user(
            username="1234567890", user_type=User.Type.PARENT
        )
        self.assertFalse(regular_user.is_staff)

    def test_string_representation(self):
        """
        Test the string representation of a user object.
        """
        user = self.User.objects.create_user(
            username="1234567890", user_type=User.Type.PARENT
        )
        self.assertEqual(str(user), "1234567890")
