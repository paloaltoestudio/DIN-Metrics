from django import forms
from users.models import User


class UpdateUserForm(forms.Form):

    managers = User.objects.filter(role = 'MANAGER')
    MANAGER_CHOICES = [(manager.id, manager) for manager in managers]

    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=30, required=False)
    phone = forms.CharField(max_length=20, min_length=10, required=False)
    birthdate = forms.DateField(required=False)
    gender = forms.CharField(max_length=1, required=False)
    manager = forms.ChoiceField(choices=MANAGER_CHOICES, required=False)

