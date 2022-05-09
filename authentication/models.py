from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

class UserAdditionalInformaion(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone_no = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    year = models.PositiveIntegerField(blank=True, null=True)
    telegram_username = models.CharField(max_length=50, blank=True, null=True)