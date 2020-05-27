from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""

        email = 'enrique@email.com'
        password = 'enrique'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self) -> None:
        """Test the email for a new user is normalized."""

        email = 'enrique@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'enrique123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'enrique123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'enrique@email.com',
            'enrique'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
