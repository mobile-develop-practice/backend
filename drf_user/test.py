"""Tests for drf_user/views.py module"""
from datetime import timedelta

import pytest
from django.test import override_settings
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from drf_user.models import AuthTransaction
from drf_user.models import User

class TestLoginView(APITestCase):
    """LoginView Test"""

    def setUp(self) -> None:
        """SetUp test data"""
        self.url = '/api/user/login/'

        self.user = baker.make(
            "drf_user.User",
            username="user",
            email="user@email.com",
            name="user",
            mobile=1234569877,
            is_active=True,
        )

        self.user.set_password("pass123")
        self.user.save()

    @pytest.mark.django_db
    def test_fields_missing(self):
        """Test when API was called without fields then it raises 400"""
        response = self.client.post(self.url, data={})
        self.assertEqual(400, response.status_code)
        self.assertIn(User.USERNAME_FIELD, response.data)
        self.assertIn("password", response.data)

    @pytest.mark.django_db
    def test_object_created(self):
        """Check if the User object is created or not"""
        self.assertEqual(1, User.objects.count())

    @pytest.mark.django_db
    def test_successful_login_view(self):
        """Check if the credentials are correct"""
        response = self.client.post(
            self.url, data={"username": "user", "password": "pass123"}
        )
        self.assertEqual(200, response.status_code)
        self.assertIn("token", response.data)
        self.assertIn("refresh_token", response.data)

        # verify that auth transaction object created
        self.assertEqual(1, AuthTransaction.objects.count())

class TestRegisterView(APITestCase):
    """RegisterView Test"""

    def setUp(self) -> None:
        """SetUp test data"""
        self.url = '/api/user/register/'
        self.validated_data = {
            "username": "my_username",
            "password": "test_password",
            "name": "random_name",
            "email": "random@django.com",
            "mobile": 1234567890,
        }
        self.not_validated_data = {
            "username": "random",
            "password": "test_password",
            "name": "random_name",
            "email": "random@example.com",
            "mobile": 8800880080,
        }

        self.data_without_mobile = {
            "username": "jake123",
            "password": "test_password",
            "name": "jake",
            "email": "random@django.com",
        }
