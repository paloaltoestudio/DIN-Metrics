from django.views.generic import UpdateView
from django.urls import reverse_lazy

#Models
from .models import SJ, CMJ, DROPS, Q
from users.models import Athlete

class NeuroBase:
    pk_url_kwarg = 'id'
    fields = ['date', 'score', ]

    # def get_object(self, queryset=None):
    #     athlete = Athlete.objects.get(id = self.kwargs.get(self.pk_url_kwarg))
    #     if queryset is None:
    #         queryset = self.get_queryset()

    #     obj = queryset.get_or_create(athlete = athlete)[0]
    #     return obj

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:jump_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class SJUpdateView(NeuroBase, UpdateView):
    model = SJ


class CMJUpdateView(NeuroBase, UpdateView):
    model = CMJ


class DROPSUpdateView(NeuroBase, UpdateView):
    model = DROPS


class QUpdateView(NeuroBase, UpdateView):
    model = Q
    
