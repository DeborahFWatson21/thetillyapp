"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def business_logo_file_path(instance, filename):
    """Generate file path for new business logo image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

def profile_image_file_path(instance, filename):
    """Generate file path for profile image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now())

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    profile_image = models.ImageField(null=True, upload_to=profile_image_file_path)

    def __str__(self):
        return '{} {}'.formate(self.user.name)

class Address(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    def __self__(self):
        return str(self.id)
3

class Business(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    date_created = models.DateField(default=timezone.now())
    slogan = models.TextField(blank=True)
    website = models.URLField(blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(null=True, upload_to=business_logo_file_path, blank=True)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    SOCIAL_MEDIA_CHOICES = (
        ('Facebook', 'Facebook'),('Twitter', 'Twitter'),('Tik Tok', 'Tik Tok'),('Instagram', 'Instagram'), ('YouTube', 'YouTube'), ('Other', 'Other')
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    social_media_link = models.URLField(blank=True)
    social_media = models.CharField(max_length=10, choices=SOCIAL_MEDIA_CHOICES, default='Facebook')

    def __str__(self):
        return '{} {}'.formate(self.social_media, self.business.name)

class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    number = models.CharField(max_length=15, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    item = models.CharField(max_length=255, null=False)
    quantity = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.item

class ProductService(models.Model):
    name = models.CharField(max_length=255, null=False)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
    service = models.BooleanField(default=True)
    product = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    materials = models.ManyToManyField(Inventory, null=True, blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    productService = models.ForeignKey(ProductService, on_delete=models.SET_NULL, null=True)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    estimated_cost = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.id)

class Invoice(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.SET_NULL, null=True)
    updated_cost = models.CharField(max_length=255, null=False)
    amount_paid = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return str(self.id)
