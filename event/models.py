from django.db import models
from django.utils.translation import gettext_lazy as _

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
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.title)


class EventImage(models.Model):
    event = models.ForeignKey("event.Event", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="events/")

    class Meta:
        verbose_name = _("Event image")
        verbose_name_plural = _("Event images")

    def __str__(self):
        return str(self.event)
