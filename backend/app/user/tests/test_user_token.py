"""
Test User token authentication
"""
from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.serializers import AuthTokenSerializer

TOKEN_URL = reverse("user:token")

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicTokenTest(TestCase):
    """Test generate user token for login"""
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user_details = {
            "username": "example",
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Example first",
            "last_name": "Example last",
            "dob": date(1998,7,6),
            "country": "United Kingdom"
        }
        
        
    def test_create_user_token(self):
        """Test generate user token for authentication"""
        
        create_user(**self.user_details)
        login_payload = {
            "username": self.user_details["username"],
            "password": self.user_details["password"]
        }
        
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_bad_login_credentials(self):
        """Test bad login credentials"""
        
        create_user(**self.user_details)
        login_payload = {
            "username": self.user_details["username"],
            "password": "123"
        }
        
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_empty_login_credientials(self):
        """Test missing login credentials"""
        
        create_user(**self.user_details)
        login_payload = {
            "username": self.user_details["username"],
            "password": ""
        }
        
        res = self.client.post(TOKEN_URL, login_payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)