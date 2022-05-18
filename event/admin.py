import os
from django.contrib import admin

from .models import Event, EventImage

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        event_images = obj.eventimage_set.all()

        for event_image in event_images:
            if event_image.image:
                if os.path.isfile(event_image.image.path):
                    os.remove(event_image.image.path)

        obj.hard_delete()


@admin.register(EventImage)
class EventImagesAdmin(admin.ModelAdmin):
    pass
