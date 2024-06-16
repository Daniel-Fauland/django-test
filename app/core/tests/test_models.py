"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def setUp(self):
        self.sample_email = 'test@example.com'
        self.sample_password = 'sample123'

    def test_create_user_with_email_successfull(self):
        """Test creating a user with an email is successful."""
        email = self.sample_email
        password = self.sample_password
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email, self.sample_password)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', self.sample_password)

    def test_new_superuser_without_email_raises_error(self):
        """Test that creating a superuser without an email
           raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser('', self.sample_password)

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            self.sample_email,
            self.sample_password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
