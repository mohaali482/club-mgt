from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Division
from .forms import DivisionForm

# Create your views here.


class DivisionCreateView(CreateView):
    model = Division
    template_name = "forms.html"
    form_class = DivisionForm
    success_url = reverse_lazy("division-list")


class DivisionDetailView(DetailView):
    model = Division
    template_name = "profile/detail.html"
    queryset = Division.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division


class DivisionListView(ListView):
    model = Division
    template_name = "list.html"
    paginate_by = 5
    queryset = Division.objects.filter(active=True)


class DivisionDeleteView(DeleteView):
    model = Division
    template_name = "delete.html"
    success_url = reverse_lazy("division-list")
    queryset = Division.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division


class DivisionUpdateView(UpdateView):
    model = Division
    template_name = "forms.html"
    form_class = DivisionForm
    success_url = reverse_lazy("division-list")
    queryset = Division.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        did64 = self.kwargs.get("id")
        did = force_str(urlsafe_base64_decode(did64))
        division = get_object_or_404(self.queryset, pk=did)

        return division
