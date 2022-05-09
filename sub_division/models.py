from django.db import models

# Create your models here.


class SubDivision(models.Model):
    division = models.ForeignKey("division.Division", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
