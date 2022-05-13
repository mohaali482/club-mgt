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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(
            is_active=True, divisionhead__isnull=True,))
        self.fields['division'] = forms.ModelChoiceField(queryset=Division.objects.filter(
            active=True, divisionhead__isnull=True))
