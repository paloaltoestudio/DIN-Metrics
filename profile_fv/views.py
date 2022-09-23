from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy

#Models
from .models import Profile_fv

class ProfileBase:
    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:profile_fv_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class ProfileUpdateView(ProfileBase, UpdateView):
    model = Profile_fv
    fields = ['weight', 'speed1', 'speed2', 'speed3', 'speed4']
    pk_url_kwarg = 'id'


class ProfileCreateView(ProfileBase, CreateView):
    model = Profile_fv
    fields = ['athlete', 'weight', 'speed1', 'speed2', 'speed3', 'speed4']
