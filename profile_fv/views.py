from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy

#Models
from .models import Profile_fv

class ProfileUpdateView(UpdateView):
    model = Profile_fv
    fields = ['weight', 'speed1', 'speed2', 'speed3', 'speed4']
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:user_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        url = url + '?tab=profile'
        return url
