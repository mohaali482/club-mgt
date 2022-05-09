from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
