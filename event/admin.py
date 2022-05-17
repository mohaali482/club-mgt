from django.contrib import admin
from .models import Event, EventImages

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventImages)
class EventImagesAdmin(admin.ModelAdmin):
    pass
