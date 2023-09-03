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
class UserManager(BaseUserManager):
    """Custom User manager"""

    def create_user(self, username, email, password, dob=date.today(),**kwargs):
        """Create new user"""
        missing_details = []
        
        if not email: 
            missing_details.append("email")
        if not username:
            missing_details.append("username")
        if not password:
            missing_details.append("password")
            
        if missing_details:
            raise ValueError(f"Please provide {', '.join(missing_details)}")
        
        user = self.model(username=username, email=self.normalize_email(email), dob=dob, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_staff(self,username,email,password, **kwargs):
        """Create staff user"""
        staff = self.create_user(username,email, password, **kwargs)
        staff.is_staff = True
        staff.save(using=self.db)
        
        return staff
    
    def create_superuser(self, username, email, password, **kwargs):
        """Create Super user"""
        super_user = self.create_user(username, email, password, **kwargs)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using=self.db)
        
        return super_user
        
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    username = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    dob = models.DateField(
        _("Date of Birth"),
        auto_now=False,
        auto_now_add=False,
    )
    country = models.CharField(_("Country"), max_length=50)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is superuser"), default=False)
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
        year_difference = today_date.year - user_dob.year
        age = year_difference + int(is_before_birthday)
        return age
    
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return str(self.username)
