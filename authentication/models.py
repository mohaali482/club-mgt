from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ("Male", "male"),
    ("Female", "female"),
]

class UserAdditionalInformaion(models.Model):
    phone_no = models.PhoneNumberField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    year = models.PositiveIntegerField()
    telegram_username = models.CharField(max_length=50)