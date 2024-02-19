from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class HolmesUserManagerTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email="test@example.com", password="password")
        self.assertEqual(user.email, "test@example.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email="admin@example.com", password="password")
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_with_non_staff(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="admin@example.com", password="password", is_staff=False)

    def test_create_superuser_with_non_superuser(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="admin@example.com", password="password", is_superuser=False)

    def test_create_user_with_blank_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="password")

    def test_create_user_with_existing_email(self):
        User.objects.create_user(email="test@example.com", password="password")

        with self.assertRaises(IntegrityError):
            User.objects.create_user(email="test@example.com", password="password")



class UserTestCase(TestCase):
    def test_user_str_method(self):
        user = User.objects.create_user(email="test@example.com", password="password")
        self.assertEqual(str(user), "test@example.com")
