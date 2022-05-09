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
        return str(self.user)

class UserDivision(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    division = models.ForeignKey("division.Division", on_delete=models.CASCADE, blank=True, null=True)
    sub_division = models.ForeignKey("sub_division.SubDivision", on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
