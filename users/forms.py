from django import forms
from users.models import User, Athlete


# class UpdateUserForm(forms.Form):

#     managers = User.objects.filter(role = 'MANAGER')
#     MANAGER_CHOICES = [(manager.id, manager) for manager in managers]

#     first_name = forms.CharField(max_length=20, required=False)
#     last_name = forms.CharField(max_length=20, required=False)
#     document = forms.IntegerField(required=False)
#     email = forms.EmailField(max_length=30, required=False)
#     phone = forms.CharField(max_length=20, min_length=10, required=False)
#     birthdate = forms.DateField(required=False)
#     gender = forms.CharField(max_length=1, required=False)
#     manager = forms.ChoiceField(choices=MANAGER_CHOICES, required=False)
#     team = forms.CharField(max_length=30, required=False)
#     sport = forms.CharField(max_length=30, required=False)
#     size = forms.CharField(max_length=10, required=False)
#     weight = forms.CharField(max_length=6, required=False)
#     eps = forms.CharField(max_length=30, required=False)

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'document', 'email', 'phone']


    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False


class UpdateAthletePersonal(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['age', 'birthdate', 'gender']


class UpdateAthleteSport(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['team', 'sport']


class UpdateAthleteMeasures(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['size', 'weight']


class UpdateAthleteHealth(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['eps', ]


class UpdateAthleteLegal(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['manager', ]