from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy

#Models
from .models import FV, FV_register

class ProfileBase:
    def get_success_url(self):
        id = self.request.POST['uid']
        fv_id = self.request.POST['profile_fv']
        success_url = reverse_lazy('users:fv_detail', kwargs = {'id': id}) + '?fv_id=' + fv_id
        url = success_url.format(**self.object.__dict__)
        return url


class ProfileUpdateView(ProfileBase, UpdateView):
    model = FV_register
    fields = ['weight', 'speed1', 'speed2', 'speed3', 'speed4']
    pk_url_kwarg = 'id'


class ProfileCreateView(ProfileBase, CreateView):
    model = FV_register
    fields = ['profile_fv', 'weight', 'speed1', 'speed2', 'speed3', 'speed4']
