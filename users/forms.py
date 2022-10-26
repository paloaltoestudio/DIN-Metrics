from django import forms
from users.models import User, Athlete

class PictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['picture',]


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