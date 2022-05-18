from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import (EventForm, EventImageForm, EventImageFormset,
                    EventImageUpdateFormset)
from .models import Event, EventImage

# Create your views here.


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "forms.html"
    success_url = reverse_lazy("event-home")

    def get(self, request, *args, **kwargs):
        # pylint:disable=W0201
        self.object = None
        form = self.get_form()
        formset = EventImageFormset()
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = EventImageFormset(request.POST, request.FILES)
        if formset.is_valid() and form.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    # pylint:disable=W0221
    def form_valid(self, form, formset):
        # pylint:disable=W0201
        self.object = form.save()
        for form_2 in formset:
            instance = form_2.save(commit=False)
            instance.event = self.object
            if instance.image:
                instance.save()

        return redirect(self.get_success_url())

    def form_invalid(self, form, formset):
        # pylint:disable=W0201
        self.object = None
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class EventUpdateView(UpdateView):
    model = Event
    template_name = "formset.html"
    form_class = EventForm
    success_url = reverse_lazy("event-home")
    queryset = Event.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        eid64 = self.kwargs.get("id")
        eid = force_str(urlsafe_base64_decode(eid64))
        event = get_object_or_404(self.queryset, pk=eid)

        return event

    def get(self, request, *args, **kwargs):
        # pylint:disable=W0201
        self.object = self.get_object()
        form = self.get_form()
        formset = EventImageUpdateFormset(
            queryset=self.object.eventimage_set.all())
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        # pylint:disable=W0201
        self.object = self.get_object()
        form = self.get_form()
        formset = EventImageUpdateFormset(
            request.POST, request.FILES, queryset=self.get_object().eventimage_set.all())
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.save()
            return self.form_valid(form)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class EventListView(ListView):
    model = Event
    template_name = "list2.html"
    queryset = Event.objects.filter(active=True)
    paginate_by = 2

class EventDeleteView(DeleteView):
    model = Event
    template_name = "delete.html"
    success_url = reverse_lazy('event-home')
    queryset = Event.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        eid64 = self.kwargs.get("id")
        eid = force_str(urlsafe_base64_decode(eid64))
        event = get_object_or_404(self.queryset, pk=eid)

        return event

class EventDetailView(DetailView):
    model = Event
    template_name = "profile/detail.html"
    queryset = Event.objects.filter(active=True)

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        eid64 = self.kwargs.get("id")
        eid = force_str(urlsafe_base64_decode(eid64))
        event = get_object_or_404(self.queryset, pk=eid)

        return event
