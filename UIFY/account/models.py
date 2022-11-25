from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.dispatch import receiver

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save()
        return user


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex='^\\+?[1-9][0-9]{7,14}$"', message='phone number must be entered')
    phone = models.CharField('phone', validators=[
                             phone_regex], max_length=12, unique=True)
    phone_verified = models.BooleanField('phone_verified', default=False)
    full_name = models.CharField('full_name', max_length=100)

  #  REQUIRED_FIELDS = ['full_name']


objects = UserManager()
