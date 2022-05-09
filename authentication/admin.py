from django.contrib import admin

from .models import UserAdditionalInformation

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
