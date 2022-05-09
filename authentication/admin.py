from .models import UserAdditionalInformation
from django.contrib import admin

# Register your models here.


@admin.register(UserAdditionalInformation)
class UserAdditionalInformationAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone_no',
        'gender',
        'year',
    ]
    list_filter = [
        'gender',
        'year'
    ]
