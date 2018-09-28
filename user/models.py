import os

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from common.utils import make_path, random_string
from common.models.fields import EmailLowerCaseField


def avatar_path(instance, filename):
    assert isinstance(instance, User)
    return make_path(os.path.join('user', 'avatar'), filename)


def gen_user_token():
    return random_string(n=20)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = EmailLowerCaseField(max_length=255, unique=True, verbose_name=_('email'))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('name'))
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_path)

    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('is superuser'))

    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_('date joined'))
    token = models.CharField(max_length=32, default=gen_user_token, verbose_name=_('temporary token'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        unique_together = ('email', 'token')

    def __str__(self):
        return self.name or self.email or self.pk

    @staticmethod
    def gen_token():
        return gen_user_token()


class SubscribeList(models.Model):
    email = models.EmailField(verbose_name=_('email'))
    token = models.CharField(default=gen_user_token, max_length=20, verbose_name=_('token'))
    date_created = models.DateTimeField(default=timezone.now, verbose_name=_('date created'))
    invited = models.BooleanField(default=False, verbose_name=_('invited'))

    class Meta:
        unique_together = ('email', 'token')
        verbose_name_plural = 'Android wait list'

    def __str__(self):
        return str(self.email)


class ContactForm(models.Model):
    email = models.EmailField(verbose_name=_('email'))
    name = models.CharField(max_length=128, verbose_name=_('name'))
    message = models.TextField(verbose_name=_('message'))
    date_created = models.DateTimeField(default=timezone.now, verbose_name=_('date created'))

    def __str__(self):
        return str(self.email)
