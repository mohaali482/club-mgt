from django import forms
from .models import SubDivision


class SubDivisionForm(forms.ModelForm):

    class Meta:
        model = SubDivision
        fields = ("name", "division", "description")
