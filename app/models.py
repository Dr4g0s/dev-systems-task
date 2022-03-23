from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from app.managers import UserManager
from app.utils import validate_image_extension, birthdate_validator


class User(AbstractUser):
    """Default user model."""

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    country_code = models.CharField('Country code', max_length=4)
    phone_number = PhoneNumberField(
        unique=True,
        help_text='Must be in E.164 format i.e. +xxxxxxxxxxx.'
    )
    gender = models.CharField(
        'Gender',
        choices=GENDER_CHOICES,
        max_length=6,
        help_text='Choose between (male, female).'
    )
    birthdate = models.DateField(
        'Birth date',
        validators=[birthdate_validator],
        help_text='Must be in format YYYY-MM-DD. Must be in the past'
    )
    avatar = models.ImageField(
        'Avatar',
        upload_to='avatars/',
        validators=[validate_image_extension],
        help_text='Supported content types: jpg, jpeg, png.')
    email = models.EmailField('Email', null=True, blank=True)
    
    objects = UserManager()

    username = None
    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return f'{self.phone_number}'


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField()

    def __str__(self):
        return f'{self.user}'
