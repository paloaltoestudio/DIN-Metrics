from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

#Models
from osteo.models import Osteo
from users.models import Athlete

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

