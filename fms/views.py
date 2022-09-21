from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from users.models import Athlete
from fms.models import Fms

class FmsBase:
    model = Fms
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        athlete = Athlete.objects.get(id = self.request.POST['id'])
        
        if queryset is None:
            queryset = self.get_queryset()
            
        obj = queryset.get_or_create(athlete = athlete)[0]
        return obj

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        #return render(self.request, 'users/detail.html', self.get_context_data(form=form))
        return redirect('users:user_detail', self.request.POST['uid'])

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fms_detail', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class FmsUpdate(FmsBase, UpdateView):
    fields = ['squat_score', 'squat_observations',
              'fence_step_l_score', 'fence_step_r_score', 'fence_step_observations',
              'lunge_l_score', 'lunge_r_score', 'lunge_observations',
              'shoulder_l_score', 'shoulder_r_score', 'shoulder_observations',
              'leg_raise_l_score', 'leg_raise_r_score', 'leg_raise_observations',
              'trunk_l_score', 'trunk_r_score', 'trunk_observations',
              'trunk_rot_l_score', 'trunk_rot_r_score', 'trunk_rot_observations']
