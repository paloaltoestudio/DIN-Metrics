from django.views.generic import UpdateView
from django.urls import reverse_lazy

#Models
from osteo.models import Osteo

class OsteoBase:
    model = Osteo
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('users:user_detail', kwargs = {'id': 10})

    def get_success_url(self):
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
            url = url + '?tab=osteo'
        
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
    # fields = ['pain', 'resting',
    #           'moving', 'on_palpitation',
    #           'zone', 'intensity',
    #           'superficial_sensitivity', 'deep_sensitivity',
    #           'inflammation', 'edema',
    #           'observations'
    #          ]

    fields = ['zone', 'intensity', 'observations']
