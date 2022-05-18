from django.db import models
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your models here.


class SubDivision(models.Model):
    division = models.ForeignKey("division.Division", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def encoded_id(self) -> str:
        encode_id = urlsafe_base64_encode(force_bytes(self.pk))
        return encode_id
