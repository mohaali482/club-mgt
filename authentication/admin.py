from django.contrib import admin

from .models import UserAdditionalInformation, UserDivision

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


@admin.register(UserDivision)
class UserDivisionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'division',
        'active',
    ]
    list_filter = [
        'division'
    ]
