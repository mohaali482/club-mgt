from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDER_CHOICES = [
    ("Male", "male"),
    ("Female", "female"),
]

class UserAdditionalInformaion(models.Model):
    phone_no = PhoneNumberField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    year = models.PositiveIntegerField()
    telegram_username = models.CharField(max_length=50)