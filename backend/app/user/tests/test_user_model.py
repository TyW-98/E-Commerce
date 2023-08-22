from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTest(TestCase):
    """Test Cases to test custom user model"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_details = {
            "username": "example",
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "Example first",
            "last_name": "Example last",
            "dob": date(1998,7,6)
        }
    
    def test_create_user_model(self):
        """Test creating user"""
        user = get_user_model().objects.create_user(**self.user_details)
        
        self.assertEqual(user.email, self.user_details["email"])
        self.assertEqual(user.username, self.user_details["username"])
        self.assertTrue(user.check_password(self.user_details["password"]))
        
    def test_normalised_email(self):
        """Test normalising user email"""
        sample_emails = [
            ["email1@EXAMPLE.COM", "email1@example.com"],
            ["Email2@Example.com", "Email2@example.com"],
            ["EMAIL3@EXAMPLE.COM", "EMAIL3@example.com"],
            ["email4@example.COM", "email4@example.com"]
        ]
        
        for index, (test_email, expected_email) in enumerate(sample_emails):
            test_user_details = dict(self.user_details)
            test_user_details["email"] = test_email
            test_user_details["username"] = f"example{index}"
            user = get_user_model().objects.create_user(**test_user_details)
            
            self.assertEqual(user.email, expected_email)
            
    def test_age_calculation(self):
        """Test age is correctly calculated"""
        user = get_user_model().objects.create_user(**self.user_details)
        
        today = date.today()
        test_user_dob = self.user_details["dob"]
        test_user_age = today.year - test_user_dob.year - ((today.month, today.day) < (test_user_dob.month, test_user_dob.day))
        
        self.assertEqual(user.age, test_user_age)
        
    def test_user_permission(self):
        """Test creating new user permission level"""
        user = get_user_model().objects.create_user(**self.user_details)
        
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        