from django import forms
import django_filters

#models
from .models import User

class UserFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    document = django_filters.CharFilter(lookup_expr='iexact', widget=forms.TextInput(attrs={'class': 'form-control'}))

    manager = django_filters.CharFilter( method='get_manager', widget=forms.TextInput(attrs={'class': 'form-control'}))


    def get_manager( self, qs, name, value):
        qs = qs.filter(athlete__manager__first_name__icontains = value)  
        return qs

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'manager', 'document']


class ManagerFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    document = django_filters.CharFilter(lookup_expr='iexact', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'document']

