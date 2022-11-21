from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

#Models
from .models import SJ, CMJ, DROPS, Q, NeuroObservations
from users.models import Athlete


class ObservationsBase:
    model = NeuroObservations

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:jump_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url

class NeuroObservationsView(ObservationsBase, CreateView):
    fields = ['observations', 'athlete']


class NeuroObservationsDeleteView(ObservationsBase, DeleteView):
    model = NeuroObservations
    pk_url_kwarg = 'id'


class NeuroObservationsEditView(ObservationsBase, UpdateView):
    pk_url_kwarg = 'id'
    fields = ['observations', ]


class NeuroBase:
    def post(self, request, *args, **kwargs):
        jump_type = request.POST['jump_type'].lower()
        if jump_type == 'sj':
            self.model = SJ
        elif jump_type == 'cmj':
            self.model = CMJ
        elif jump_type == 'drops':
            self.model = DROPS
        else:
            self.model = Q

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:jump_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url



class NeuroCreateBase(NeuroBase, CreateView):
    fields = ['date', 'score', 'athlete']
    

class NeuroBaseUpdate(NeuroBase, UpdateView):
    pk_url_kwarg = 'id'
    fields = ['date', 'score', ]


class NeuroDelete(DeleteView):
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        # Set self.object before the usual form processing flow.
        # Inlined because having DeletionMixin as the first base, for
        # get_success_url(), makes leveraging super() with ProcessFormView
        # overly complex.

        jump_type = request.POST['jump_type'].lower()
        print('jump: ', jump_type)
        if jump_type == 'sj':
            self.model = SJ
        elif jump_type == 'cmj':
            self.model = CMJ
        elif jump_type == 'drops':
            self.model = DROPS
        else:
            self.model = Q

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:jump_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url