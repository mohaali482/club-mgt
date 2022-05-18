from django import forms
from django.forms import formset_factory
from django.forms.models import modelformset_factory

from .models import Event, EventImage


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = [
            "active",
            "created_at",
            "updated_at"
        ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['issue_date'].widget = forms.widgets.DateTimeInput(attrs={
            'type': 'datetime-local'
        })
        self.fields['start_date'].widget = forms.widgets.DateTimeInput(attrs={
            'type': 'datetime-local'
        })
        self.fields['end_date'].widget = forms.widgets.DateTimeInput(attrs={
            'type': 'datetime-local'
        })


class EventImageForm(forms.ModelForm):

    class Meta:
        model = EventImage
        fields = ("image",)


EventImageFormset = formset_factory(EventImageForm)
EventImageUpdateFormset = modelformset_factory(EventImage, EventImageForm, extra=0, can_delete=True)
