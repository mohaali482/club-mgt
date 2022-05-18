import os
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from clubmgt.softdeletion import regenerate_field_for_soft_deletion

# Create your models here.


class Event(models.Model):
    division = models.ForeignKey("division.Division", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    issue_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def encoded_id(self) -> str:
        encode_id = urlsafe_base64_encode(force_bytes(self.pk))
        return encode_id

    def delete(self, using=None, keep_parents=False):
        # Rename the title to know when deleted
        self.title = regenerate_field_for_soft_deletion(self, 'title')
        self.active = False
        self.save()
        event_images = self.eventimage_set.all()

        for event_image in event_images:
            if event_image.image:
                if os.path.isfile(event_image.image.path):
                    os.remove(event_image.image.path)

    def hard_delete(self):
        super().delete()

    def __str__(self):
        return str(self.title)


class EventImage(models.Model):
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/", blank=True)

    class Meta:
        verbose_name = _("Event image")
        verbose_name_plural = _("Event images")

    def __str__(self):
        return str(self.event)
