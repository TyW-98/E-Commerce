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
USER_ACCOUNT_URL = reverse("user:account")
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
        res = self.client.get(USER_ACCOUNT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_create_superuser(self):
        """Test cannot create superuser"""
        res = self.client.post(CREATE_SUPERUSER_URL, self.user_details)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_cannot_create_staff(self):
        """Test cannot create staff"""
        res = self.client.post(CREATE_STAFF_URL, self.user_details)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
            

class PrivateUserAPITest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin_details = {
            "username": "admin_user",
            "email": "admin_@example.com",
            "password": "admin_password",
            "first_name": "Admin First",
            "last_name": "Admin Last",
            "dob": date(1980, 1, 1),  # Choose a suitable date
            "country": "United Kingdom",
        }
        cls.admin = get_user_model().objects.create_superuser(**cls.admin_details)
        cls.admin_client = APIClient()
        cls.admin_client.force_authenticate(user=cls.admin)

    
        cls.staff_details = {
            "username": "staff_user",
            "email": "staff_@example.com",
            "password": "staff_password",
            "first_name": "staff first",
            "last_name": "staff last",
            "dob": date(1980,1,1),
            "country": "United Kingdom"
        }
        cls.staff = get_user_model().objects.create_staff(**cls.staff_details)
        cls.staff_client = APIClient()
        cls.staff_client.force_authenticate(user=cls.staff)
    
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
        res = self.client.get(USER_ACCOUNT_URL)
        user = get_user_model().objects.get(id=self.user.id)
        serializer = UserSerializer(user, many=False)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    # def test_fetch_another_user_details(self):
    #     """Test cannot fetch another user's details""" use token isntead of user2.id
    #     user2_details = dict(self.user_details)
    #     user2_details["email"] = "test2@example.com"
    #     user2_details["username"] = "example2"
    #     user2 = create_user(**user2_details)
    #     res = self.client.get(user_specific_url(user2.id))
    #     self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_all_user_details(self):
        """Test cannot fetch all users' details"""
        res = self.client.get(ALL_USERS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_create_superuser(self):
        """Test creating superuser"""
        payload = dict(self.admin_details)
        payload["email"] = "admin2@example.com"
        payload["username"] = "admin2"
        res = self.admin_client.post(CREATE_SUPERUSER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_admin = get_user_model().objects.get(username=payload["username"])
        self.assertTrue(test_admin.is_superuser)
        self.assertTrue(test_admin.is_staff)
        
    def test_create_staff(self):
        """Test creating staff user"""
        payload = dict(self.staff_details)
        payload["email"] = "staff@example.com"
        payload["username"] = "staff2"
        res = self.staff_client.post(CREATE_STAFF_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        test_staff = get_user_model().objects.get(username=payload["username"])
        self.assertTrue(test_staff.is_staff)
        self.assertFalse(test_staff.is_superuser)
        
    def ttest_authenticated_create_superuser(self):
        """Test authenticated user cannot create superuser"""
        payload = dict(self.user_details)
        payload["email"] = "testadmin@example.com"
        payload["username"] = "testadmin"
        res = self.client.post(CREATE_SUPERUSER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        is_created = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(is_created)
        
    def test_authenticated_create_staff(self):
        """Test authenticated user cannot create staff"""
        payload = dict(self.user_details)
        payload["email"] = "teststaff@example.com"
        payload["username"] = "teststaff"
        res = self.client.post(CREATE_STAFF_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        is_created = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(is_created)
        
    def test_staff_create_superuser(self):
        """Test staff user cannot create superuser"""
        payload = dict(self.admin_details)
        payload["email"] = "admin2@example.com"
        payload["username"] = "admin2@example.com"
        res = self.staff_client.post(CREATE_SUPERUSER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_update_user_details(self):
        """Test updating user's information"""
        patch_payload = {
            "first_name": "Update First",
            "last_name": "Update Last",
            "password": "Updatedpassword"
        }
        res = self.client.patch(USER_ACCOUNT_URL, patch_payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        self.user.refresh_from_db()
        self.assertEqual(
        {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name
        },
        {
            "first_name": patch_payload["first_name"],
            "last_name": patch_payload["last_name"]
        }
        )
        self.assertTrue(self.user.check_password(patch_payload["password"]))
        
    def test_delete_user(self):
        """Test deleting user's account"""
        res = self.client.delete(USER_ACCOUNT_URL)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        deleted_user = get_user_model().objects.filter(email=self.user_details["email"]).exists()
        self.assertFalse(deleted_user)
        
        

# TODO :  admin dashboard setup, account delete, token creation validationS