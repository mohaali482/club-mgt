from django.contrib import admin

from .forms import DivisionForm, DivisionHeadForm
from .models import Division, DivisionHead, DivisionHeadHistory

# Register your models here.


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
    )
    form = DivisionForm

    def get_queryset(self, request):
        queryset = self.model.admin_page
        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset


@admin.register(DivisionHead)
class DivisionHeadAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "division",
    )
    form = DivisionHeadForm


@admin.register(DivisionHeadHistory)
class DivisionHeadHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "division",
        "started_date",
        "ended_date",
    )
