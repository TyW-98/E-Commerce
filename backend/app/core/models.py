from datetime import date

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    username = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(_(""), default=True)
    is_staff = models.BooleanField(_(""), default=False)
    is_superuser = models.BooleanField(_(""), default=False)
    joined_date = models.DateField(_("Joined Date"), auto_now_add=True)
    last_login = models.DateField(_("Last Online"), auto_now_add=True)
    
    @property
    def age(self):
        today_date = date.today()
        user_dob = self.dob
        # If true returns 1 else 0
        is_before_birthday = (
            today_date.month, today_date.day
        ) < (user_dob.month, user_dob.day)
        year_difference = today_date - user_dob
        age = year_difference + int(is_before_birthday)
        return age
    
    USERNAME_FIELD = "username"
    
    def __str__(self):
        return f"{self.username}"
        
    
    
