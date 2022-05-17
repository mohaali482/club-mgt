from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
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


class AdminDivisionQuerySet(models.QuerySet):
    pass


class DivisionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.admin_page = kwargs.pop("admin_page", False)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.admin_page:
            return AdminDivisionQuerySet(self.model, using=self._db)

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
    admin_page = DivisionManager(admin_page=True)

    def __str__(self):
        return str(self.name)

    def encoded_id(self) -> str:
        encode_id = urlsafe_base64_encode(force_bytes(self.pk))
        return encode_id

    def delete(self, using=None, keep_parents=False):
        # Rename the name to prevent collision
        self.name = regenerate_field_for_soft_deletion(self, 'name')
        self.active = False
        self.save()

    def hard_delete(self):
        return super().delete(self)


class DivisionHeadQuerySet(models.QuerySet):
    def delete(self):
        for division_head in super().all():
            division_head_history = DivisionHeadHistory()
            division_head_history.user = division_head.user
            division_head_history.division = division_head.division
            division_head_history.started_date = division_head.created_at
            division_head_history.ended_date = timezone.now()
            division_head_history.save()

        return super().delete()


class DivisionHeadManager(models.Manager):
    def get_queryset(self):
        return DivisionHeadQuerySet(self.model, using=self._db)


class DivisionHead(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    division = models.OneToOneField(
        "division.Division", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DivisionHeadManager()

    def __str__(self) -> str:
        return str(self.user)

    def encoded_id(self) -> str:
        encode_id = urlsafe_base64_encode(force_bytes(self.pk))
        return encode_id


class DivisionHeadHistory(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    division = models.ForeignKey("division.Division", on_delete=models.CASCADE)
    started_date = models.DateTimeField()
    ended_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Division Head History")
        verbose_name_plural = _("Division Head Histories")

    def __str__(self):
        return f'{self.user} head of {self.division}'
