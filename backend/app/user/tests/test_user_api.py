"""
Test User API
"""
from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.serializers import UserSerializer

ALL_USERS_URL = reverse("user:user-list")
CREATE_USER_URL = reverse("user:create-user")
USER_ACCOUNT_DETAILS_URL = reverse("user:user-fetch-user-details")


def create_user(**params):
    """Create user"""
    return get_user_model().objects.create_user(**params)

def user_specific_url(user_id): 
    """Create dynamic user detail URL"""
    return reverse("user:delete-detail",args=[user_id])


class PublicUserAPITest(TestCase):
    
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
    
    def setUp(self):
        self.client = APIClient()
        
    def test_create_user(self):
        """Test creating new user"""
        payload = self.user_details
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])

        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)
        
    def test_unique_email(self):
        """Test creating user with duplicate email and username"""
        create_user(**self.user_details)
        res = self.client.post(CREATE_USER_URL, self.user_details)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_password_length(self):
        """Test creating user with password too short"""
        payload = dict(self.user_details)
        payload["password"] = "pass"
        res = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_created = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_created)
        
    def test_missing_details(self):
        """Test missing details when creating new user"""
        fields = ["username", "email", "password"]
        
        for field in fields:
            payload = dict(self.user_details)
            payload[field] = ""
            
            res = self.client.post(CREATE_USER_URL, payload)
            self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
            
    def test_error_fetch_user(self):
        """Test cannot fetch users data if not admin or staff"""
        res = self.client.get(ALL_USERS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
            

class PrivateUserAPITest(TestCase):
    
    def setUp(self):
        user_details = {
            "username": "example",
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Example first",
            "last_name": "Example last",
            "dob": date(1998,7,6),
            "country": "United Kingdom"
        }
        self.user = get_user_model().objects.create_user(**user_details)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
    
    def test_fetch_user_details(self):
        res = self.client.get(USER_ACCOUNT_DETAILS_URL)
        user = get_user_model().objects.get(id=self.user.id)
        serializer = UserSerializer(user, many=False)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

# TODO : fetching another user's detail error, creating superuser, creating staff, admin dashboard setup, update account details, account delete, change password, token creation validation