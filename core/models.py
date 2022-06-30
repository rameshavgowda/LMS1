from xml.etree.ElementTree import TreeBuilder
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#create your model here

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("please provide email")
        if not password:
            raise ValueError("please provide password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name if self.name else self.email


class Book(models.Model):

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    Isbn = models.CharField(max_length=13, unique=True)
    Title = models.CharField(max_length=255, blank=False, null=False)
    Author = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Publisher_name = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.title