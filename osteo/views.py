from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#Models
from osteo.models import Osteo
from users.models import Athlete, User

class OsteoCreateView(CreateView):
    model = Osteo
    fields = ['athlete', 'date',]

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:osteo_detail', kwargs = {'id': id}) + '?osteo_id=' + str(self.object.pk)
        url = success_url.format(**self.object.__dict__)
        return url


class OsteoDeleteView(DeleteView):
    model = Osteo
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:osteo_list', kwargs = {'id': id})
        url = success_url.format(**self.object.__dict__)
        return url


class OsteoBase:
    model = Osteo
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.request.POST['uid']
        success_url = reverse_lazy('users:osteo_detail', kwargs = {'id': id}) + '?osteo_id=' + str(self.object.pk)
        url = success_url.format(**self.object.__dict__)
        return url


class OsteoReportView(LoginRequiredMixin, DetailView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'users/report_osteo.html'
    extra_context = {
        'page': 'user_list_detail',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Get data from osteo and make chart
        if(self.request.GET.get('osteo_id')):
            osteos = Osteo.objects.filter(athlete = context['user'].athlete)
            
            osteo_id = self.request.GET['osteo_id']
            osteo = Osteo.objects.filter(id=osteo_id)
            osteo = osteo[0]
            
            context['osteos'] = osteos
            context['osteo'] = osteo
        else:
            osteo = Osteo.objects.filter(athlete = context['user'].athlete)
            context['osteo'] = osteo[0]
            context['osteos'] = osteo


        return context


class FlexUpdate(OsteoBase, UpdateView):
    fields = ['pectoralis_minor_l', 'pectoralis_minor_r', 
              'pectoralis_major_l', 'pectoralis_major_r', 
              'shoulder_internal_rotator_l', 'shoulder_internal_rotator_r',
              'shoulder_external_rotator_l', 'shoulder_external_rotator_r',
              'psoas_iliaco_l', 'psoas_iliaco_r',
              'hip_adductors_l', 'hip_adductors_r',
              'tensioner_fascia_liata_l', 'tensioner_fascia_liata_r',
              'low_spinal_l', 'low_spinal_r',
              'hamstrings_l', 'hamstrings_r',
              'quadriceps_l', 'quadriceps_r',
              'achilles_tendon_l', 'achilles_tendon_r',
              'spine_lumbar'
              ]
    

class MeasuresUpdate(OsteoBase, UpdateView):
    fields = ['real_upper_l', 'real_upper_r',
              'real_lower_l', 'real_lower_r',
              'apparent_upper_l', 'apparent_upper_r',
              'apparent_lower_l', 'apparent_lower_r',
              'arm_l_mt', 'arm_r_mt',
              'forearm_l_mt', 'forearm_r_mt',
              'thigh_l_mt', 'thigh_r_mt',
              'leg_l_mt', 'leg_r_mt'
             ]
class PainUpdate(OsteoBase, UpdateView):
    fields = ['pain', 'resting',
              'moving', 'on_palpitation',
              'zone', 'intensity',
              'superficial_sensitivity', 'deep_sensitivity',
              'inflammation', 'edema',
              'observations'
             ]

