from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import PhoneValidator

class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[PhoneValidator()], unique=True)
    country = models.CharField(max_length=125, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    # country = models.CharField(max_length=100, null=True, blank=True)
    # address = models.TextField(null=True, blank=True)
    # city = models.CharField(max_length=100, null=True, blank=True)
    # region = models.CharField(max_length=100, null=True, blank=True)
    # zip_code = models.CharField(max_length=6, null=True, blank=True)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
# class ProfileModel(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#     country = models.CharField(max_length=125, null=True, blank=True)
#     address1 = models.CharField(max_length=255, null=True, blank=True)
#     address2 = models.CharField(max_length=255, null=True, blank=True)
#     city = models.CharField(max_length=100, null=True, blank=True)
#     state = models.CharField(max_length=100, null=True, blank=True)
#     zip_code = models.CharField(max_length=6, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'pfofile'
#         verbose_name_plural = 'profiles'

