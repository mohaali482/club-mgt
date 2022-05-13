from django.contrib import admin
from .models import SubDivision
# Register your models here.

@admin.register(SubDivision)
class SubDivisionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "division",
        "active"
    )

    list_filter = (
        "division",
        "active"
    )
