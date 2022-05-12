from django.contrib import admin
from .models import Division, DivisionHead, AdminDivisionQuerySet
from .forms import DivisionHeadForm, DivisionForm

# Register your models here.


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "active",
    )
    form = DivisionForm

    def get_queryset(self, request):
        qs = self.model.admin_page
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
    


@admin.register(DivisionHead)
class DivisionHeadAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "division",
        "active",
    )
    form = DivisionHeadForm
