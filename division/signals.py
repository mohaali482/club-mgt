from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import DivisionHead, DivisionHeadHistory


@receiver(pre_delete, sender=DivisionHead)
def create_division_history(sender, instance, using, **kwargs):
    DivisionHeadHistory.objects.create(
        user=instance.user,
        division=instance.division,
        started_date=instance.created_at,
        ended_date=timezone.now()
    )
