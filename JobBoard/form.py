from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Company

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'Phone', 'birth_date', 'password1', 'password2']


class CompanyFilterForm(forms.Form):
    sector_choices = Company.objects.values_list('sector', 'sector').distinct()
    sector = forms.ChoiceField(choices=[('', 'All')] + list(sector_choices), required=False)
