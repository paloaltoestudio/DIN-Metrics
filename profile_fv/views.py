from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

#Models
from .models import FV, FV_register, FV_observation

#utils
from users.data.fv_data import fv_data


class ProfileObservationBase:
    model = FV_observation

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:profile_fv_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class ProfileObservationsUpdateView(ProfileObservationBase, UpdateView):
    fields = ['observation',]
    pk_url_kwarg = 'id'


class ProfileObservationsCreateView(ProfileObservationBase, CreateView):
    fields = ['athlete', 'observation',]


class ProfileObservationsDeleteView(ProfileObservationBase, DeleteView):
    pk_url_kwarg = 'id'


class FVBase:
    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fv_detail', kwargs = {'id': id}) + '?fv_id=' + str(self.object.pk)
        url = success_url.format(**self.object.__dict__)
        return url


def get_data(self, context):
    fv_id = self.request.POST['profile_fv']
    rm = fv_data(fv_id, context)
    fv = FV.objects.filter(id=fv_id)
    fv = fv[0]
    fv.rm = rm
    fv.save()

class ProfileCreateBase:
    def form_valid(self, form, **kwargs):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        context = super().get_context_data(**kwargs)
        get_data(self, context)

        return super().form_valid(form)


class ProfileDeleteBase:
    def form_valid(self, form, **kwargs):
        success_url = self.get_success_url()
        self.object.delete()
        context = super().get_context_data(**kwargs)
        get_data(self, context)
        return HttpResponseRedirect(success_url)


class ProfileBase:
    def get_success_url(self):
        id = self.request.POST['uid']
        fv_id = self.request.POST['profile_fv']
        success_url = reverse_lazy('users:fv_detail', kwargs = {'id': id}) + '?fv_id=' + fv_id
        url = success_url.format(**self.object.__dict__)
        return url


class FVCreateView(FVBase, CreateView):
    model = FV
    fields = ['athlete', 'date',]


class FVDelete(ProfileBase, DeleteView):
    model = FV
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:profile_fv_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class ProfileUpdateView(ProfileBase, ProfileCreateBase, UpdateView):
    model = FV_register
    fields = ['weight', 'speed1', 'speed2', 'speed3', 'speed4']
    pk_url_kwarg = 'id'


class ProfileCreateView(ProfileBase, ProfileCreateBase, CreateView):
    model = FV_register
    fields = ['profile_fv', 'weight', 'speed1', 'speed2', 'speed3', 'speed4']


class ProfileDelete(ProfileBase, ProfileDeleteBase, DeleteView):
    model = FV_register
    pk_url_kwarg = 'id'
