from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    Admin = 1
    Teacher = 2
    Student = 3
    ROLE_CHOICES = (
        (Admin, 'Admin'),
        (Teacher, 'Teacher'),
        (Student, 'Student'),
    )
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="images/", default="", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE_CHOICES,
                            default=3, max_length=15, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    USERNAME_FIELD = "username"
    objects = CustomUserManager()


class ContactDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primary_phone = models.IntegerField(blank=True, null=True)
    secondary_phone = models.IntegerField(null=True, blank=True)
    primary_email = models.EmailField(null=True, blank=True)
    secondary_email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
