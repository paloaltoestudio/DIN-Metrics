from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from users.models import Athlete
from fms.models import Fms

#Utils
from users.utils import age, get_sum

class FmsBase:
    model = Fms
    pk_url_kwarg = 'id'

    

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        #return render(self.request, 'users/detail.html', self.get_context_data(form=form))
        return redirect('users:user_detail', self.request.POST['uid'])

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        def check_value(value):
                if type(value) != int:
                    return 0
                else:
                    return value

        fence_total = get_sum(check_value(form.instance.fence_step_l_score), check_value(form.instance.fence_step_r_score))
        lunge_total = get_sum(check_value(form.instance.lunge_l_score), check_value(form.instance.lunge_r_score))
        shoulder_total = get_sum(check_value(form.instance.shoulder_l_score), check_value(form.instance.shoulder_r_score))
        leg_total = get_sum(check_value(form.instance.leg_raise_l_score), check_value(form.instance.leg_raise_r_score))
        trunk_total = get_sum(check_value(form.instance.trunk_l_score), check_value(form.instance.trunk_r_score))
        trunk_rot_total = get_sum(check_value(form.instance.trunk_rot_l_score), check_value(form.instance.trunk_rot_r_score))

        form.instance.total = sum([check_value(form.instance.squat_score), check_value(fence_total), check_value(lunge_total), check_value(shoulder_total), 
                            check_value(leg_total), check_value(trunk_total), check_value(trunk_rot_total)])

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fms_detail', kwargs = {'id': id}) + '?fms_id=' + str(self.object.pk)
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


class FMSCreateView(CreateView):
    model = Fms
    fields = ['athlete', 'date',]

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fms_detail', kwargs = {'id': id}) + '?fms_id=' + str(self.object.pk)
        url = success_url.format(**self.object.__dict__)
        return url


class FMSDeleteView(DeleteView):
    model = Fms
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:fms_list', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url