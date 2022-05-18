from django import forms
from django.contrib.auth.models import User

from .models import Division, DivisionHead


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ("name", "description",)


class DivisionHeadForm(forms.ModelForm):

    class Meta:
        model = DivisionHead
        fields = ("user", "division")
