from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import DivisionForm, DivisionHeadForm
from .models import Division, DivisionHead

# Create your views here.


class DivisionCreateView(PermissionRequiredMixin, CreateView):
    model = Division
    template_name = "forms.html"
    form_class = DivisionForm
    success_url = reverse_lazy("division-list")

    permission_required = ("division.add_division")


class DivisionDetailView(PermissionRequiredMixin, DetailView):
    model = Division
    template_name = "profile/detail.html"
    queryset = Division.objects.filter(active=True)
    permission_required = ("division.view_division")

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division


class DivisionListView(PermissionRequiredMixin, ListView):
    model = Division
    template_name = "list.html"
    paginate_by = 5
    queryset = Division.objects.filter(active=True)

    permission_required = ("division.view_division")


class DivisionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Division
    template_name = "delete.html"
    success_url = reverse_lazy("division-list")
    queryset = Division.objects.filter(active=True)
    permission_required = ("division.delete_division")

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division


class DivisionUpdateView(PermissionRequiredMixin, UpdateView):
    model = Division
    template_name = "forms.html"
    form_class = DivisionForm
    success_url = reverse_lazy("division-list")
    queryset = Division.objects.filter(active=True)
    permission_required = ("division.change_division")

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division


class DivisionHeadCreateView(PermissionRequiredMixin, CreateView):
    model = DivisionHead
    form_class = DivisionHeadForm
    template_name = "forms.html"
    permission_required = (
        "division.add_divisionhead"
    )
    success_url = reverse_lazy("division-list")


class DivisionHeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = DivisionHead
    template_name = "delete.html"
    permission_required = (
        "division.delete_divisionhead"
    )
    queryset = DivisionHead.objects.all()
    success_url = reverse_lazy("division-list")

    def get_object(self, queryset=None):
        dhid64 = self.kwargs.get("id")
        dhid = force_str(urlsafe_base64_decode(dhid64))
        division_head = get_object_or_404(self.queryset, pk=dhid)

        return division_head


class DivisionHeadListView(PermissionRequiredMixin, ListView):
    model = DivisionHead
    template_name = "list.html"
    paginate_by = 10

    permission_required = (
        "division.view_divisionhead"
    )
