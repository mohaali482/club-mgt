import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Event, EventImage

@receiver(pre_save, sender=EventImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = EventImage.objects.get(pk=instance.pk).image
    except EventImage.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    return True
