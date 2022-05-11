from django.contrib import admin
from .models import Division

# Register your models here.

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    pass
