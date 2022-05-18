from django.contrib import admin

from .models import Event, EventImage

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(EventImage)
class EventImagesAdmin(admin.ModelAdmin):
    pass
