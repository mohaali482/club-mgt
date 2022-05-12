from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from clubmgt.softdeletion import regenerate_field_for_soft_deletion
# Create your models here.


class DivisionQuerySet(models.QuerySet):
    def delete(self):
        return super().update(active=False)

    # if needed
    def hard_delete(self):
        return super().delete()

    def active_all(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = Q(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        return self.filter(lookups)


class DivisionManager(models.Manager):
    def get_queryset(self):
        return DivisionQuerySet(self.model, using=self._db)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class Division(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DivisionManager()

    def __str__(self):
        return str(self.name)

    def encoded_id(self) -> str:
        encode_id = urlsafe_base64_encode(force_bytes(self.pk))
        return encode_id

    def delete(self, using=None, keep_parents=False):
        # Rename the name to prevent collision
        self.name = regenerate_field_for_soft_deletion(self,'name')
        self.active = False
        self.save()

    def hard_delete(self):
        return super().delete(self)
