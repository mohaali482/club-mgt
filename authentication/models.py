from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

YEAR_CHOICES = [
    (1, "First year"),
    (2, "Second year"),
    (3, "Third year"),
    (4, "Fourth year"),
    (5, "Fifth year"),
]


class UserAdditionalInformation(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone_no = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    telegram_username = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user
    
