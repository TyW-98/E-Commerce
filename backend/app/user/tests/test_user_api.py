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
CREATE_STAFF_URL = reverse("user:create-staff")
CREATE_SUPERUSER_URL = reverse("user:create-admin")


def create_user(**params):
    """Create user"""
    return get_user_model().objects.create_user(**params)

def user_specific_url(user_id): 
    """Create dynamic user detail URL"""
    return reverse("user:user-detail",args=[user_id])


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
        """Test cannot fetch all users data if not admin or staff"""
        res = self.client.get(ALL_USERS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_cannot_fetch_user_details(self):
        """Test cannot fetch any user data without authenticating"""
        auth_user = create_user(**self.user_details)
        res = self.client.get(user_specific_url(auth_user.id))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_create_superuser(self):
        """Test cannot create superuser"""
        res = self.client.post(CREATE_SUPERUSER_URL, self.user_details)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_cannot_create_staff(self):
        """Test cannot create staff"""
        res = self.client.post(CREATE_STAFF_URL, self.user_details)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
            

class PrivateUserAPITest(TestCase):
    
    def setUp(self):
        self.user_details = {
            "username": "example",
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Example first",
            "last_name": "Example last",
            "dob": date(1998,7,6),
            "country": "United Kingdom"
        }
        self.user = create_user(**self.user_details)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_fetch_user_details(self):
        """Test fetching user's details"""
        res = self.client.get(user_specific_url(self.user.id))
        user = get_user_model().objects.get(id=self.user.id)
        serializer = UserSerializer(user, many=False)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_fetch_another_user_details(self):
        """Test fetching another user's details"""
        user2_details = dict(self.user_details)
        user2_details["email"] = "test2@example.com"
        user2_details["username"] = "example2"
        user2 = create_user(**user2_details)
        res = self.client.get(user_specific_url(user2.id))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_create_superuser_authenticated(self):
        """Test authenticated user cannot create superuser"""
        payload = dict(self.user_details)
        payload["email"] = "testadmin@example.com"
        payload["username"] = "testadmin"
        res = self.client.post(CREATE_SUPERUSER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        is_created = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(is_created)
        
    def test_create_staff_authenticated(self):
        """Test authenticated user cannot create staff"""
        payload = dict(self.user_details)
        payload["email"] = "teststaff@example.com"
        payload["username"] = "teststaff"
        res = self.client.post(CREATE_STAFF_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        is_created = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(is_created)
        

# TODO :  creating superuser, creating staff, admin dashboard setup, update account details, account delete, change password, token creation validationS