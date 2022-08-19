from django import forms


class UpdateUserForm(forms.Form):
    age = forms.IntegerField(required=False)
    phone = forms.CharField(max_length=11, required=False)
    birthdate = forms.DateField(required=False)
    gender = forms.CharField(max_length=1, required=False)