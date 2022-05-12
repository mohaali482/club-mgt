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
            is_active=True, divisionhead__isnull=True))
        self.fields['division'] = forms.ModelChoiceField(queryset=Division.objects.filter(
            active=True, divisionhead__isnull=True))

    def clean_user(self):
        user = self.cleaned_data["user"]
        if User.objects.filter(is_active=True, divisionhead__isnull=True, pk=user.pk).exists():
            return user

        raise forms.ValidationError("This user is already a head")

    def clean_division(self):
        division = self.cleaned_data["division"]
        if Division.objects.filter(active=True, divisionhead__isnull=True, pk=division.pk).exists():
            return division

        raise forms.ValidationError("This division has already a head.")
