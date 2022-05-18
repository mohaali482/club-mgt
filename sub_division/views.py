from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import SubDivisionForm
from .models import SubDivision

# Create your views here.


class SubDivisionCreateView(CreateView):
    model = SubDivision
    template_name = "forms.html"
    form_class = SubDivisionForm
    success_url = reverse_lazy("sub-division-list")


class SubDivisionDeleteView(DeleteView):
    model = SubDivision
    template_name = "delete.html"
    success_url = reverse_lazy("sub-division-list")
    queryset = SubDivision.objects.filter(active=True)

    def get_object(self, queryset=None):
        sdid64 = self.kwargs.get("id")
        sdid = urlsafe_base64_decode(force_str(sdid64))
        sub_division = get_object_or_404(self.queryset, pk=sdid)
        return sub_division


class SubDivisionListView(ListView):
    model = SubDivision
    template_name = "list.html"
    queryset = SubDivision.objects.filter(active=True)


class SubDivisionDetailView(DetailView):
    model = SubDivision
    template_name = "profile/detail.html"
    queryset = SubDivision.objects.filter(active=True)

    def get_object(self, queryset=None):
        sdid64 = self.kwargs.get("id")
        sdid = urlsafe_base64_decode(force_str(sdid64))
        sub_division = get_object_or_404(self.queryset, pk=sdid)
        return sub_division


class SubDivisionUpdateView(UpdateView):
    model = SubDivision
    template_name = "forms.html"
    success_url = reverse_lazy("sub-division-list")
    form_class = SubDivisionForm

    def get_object(self, queryset=None):
        sdid64 = self.kwargs.get("id")
        sdid = urlsafe_base64_decode(force_str(sdid64))
        sub_division = get_object_or_404(self.queryset, pk=sdid)
        return sub_division
