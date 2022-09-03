from django.db import models

from users.models import Athlete

class Osteo(models.Model):
    PAIN_CHOICES = (
        ('NR', 'No Refiere'),
        ('C', 'Conservado'),
        ('A', 'Alterado'),
        ('NE', 'No Evaluado')
    )

    FLEX_CHOICES = (
        ('L', 'Leve'),
        ('M', 'Moderada'),
        ('S', 'Severa'),
        ('NE', 'No evaluado'),
        ('NR', 'No retracción')
    )

    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    pain = models.CharField('Dolor', max_length=2, choices=PAIN_CHOICES, blank=True)
    resting = models.CharField('En reposo', max_length=2, choices=PAIN_CHOICES, blank=True)
    moving = models.CharField('En movimiento', max_length=2, choices=PAIN_CHOICES, blank=True)
    on_palpitation = models.CharField('A la palpación', max_length=2, choices=PAIN_CHOICES, blank=True)
    zone = models.CharField('Zona', max_length=30, blank=True)
    intensity = models.CharField('Intensidad', max_length=30, blank=True)
    superficial_sensitivity = models.CharField('Sensibilidad superficial', max_length=2, choices=PAIN_CHOICES, blank=True)
    deep_sensitivity = models.CharField('Sensibilidad profunda', max_length=2, choices=PAIN_CHOICES, blank=True)
    inflammation = models.CharField('Inflamación', max_length=2, choices=PAIN_CHOICES, blank=True)
    edema = models.CharField('Edema', max_length=2, choices=PAIN_CHOICES, blank=True)
    observations = models.TextField('Observaciones',blank=True)
    pectoralis_minor_l = models.CharField('Pectoral menor - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    pectoralis_minor_r = models.CharField('Pectoral menor - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    pectoralis_major_l = models.CharField('Pectoral mayor - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    pectoralis_major_r = models.CharField('Pectoral mayor - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    shoulder_internal_rotator_l = models.CharField('Rotador interno de hombro - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    shoulder_internal_rotator_r = models.CharField('Rotador interno de hombro - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    shoulder_external_rotator_l = models.CharField('Rotador externo de hombro - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    shoulder_external_rotator_r = models.CharField('Rotador externo de hombro - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    psoas_iliaco_l = models.CharField('PSOAS ilíaco - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    psoas_iliaco_r = models.CharField('PSOAS ilíaco - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    hip_adductors_l = models.CharField('Aductores de cadera - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    hip_adductors_r = models.CharField('Aductores de cadera - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    tensioner_fascia_liata_l = models.CharField('Tensor de la fascia lata - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    tensioner_fascia_liata_r = models.CharField('Tensor de la fascia lata - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    low_spinal_l = models.CharField('Espinales bajos - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    low_spinal_r = models.CharField('Espinales bajos - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    hamstrings_l = models.CharField('Isquitibiales - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    hamstrings_r = models.CharField('Isquitibiales - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    quadriceps_l = models.CharField('Cuadriceps - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    quadriceps_r = models.CharField('Cuadriceps - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    achilles_tendon_l = models.CharField('Tendón de Aquiles - Izquierdo', max_length=2, choices=FLEX_CHOICES, blank=True)
    achilles_tendon_r = models.CharField('Tendón de Aquiles - Derecho', max_length=2, choices=FLEX_CHOICES, blank=True)
    spine_lumbar = models.CharField('Columna vertebral lumbar', max_length=2, choices=FLEX_CHOICES, blank=True)
    real_upper_r = models.CharField('Miembro superior derecho | Reales', max_length=10, blank=True)
    real_upper_l = models.CharField('Miembro superior izquierdo | Reales', max_length=10, blank=True)
    real_lower_r = models.CharField('Miembro inferior derecho | Reales', max_length=10, blank=True)
    real_lower_l = models.CharField('Miembro inferior izquierdo | Reales', max_length=10, blank=True)
    apparent_upper_r = models.CharField('Miembro superior derecho | Aparentes', max_length=10, blank=True)
    apparent_upper_l = models.CharField('Miembro superior izquierdo | Aparentes', max_length=10, blank=True)
    apparent_lower_r = models.CharField('Miembro inferior derecho | Aparentes', max_length=10, blank=True)
    apparent_lower_l = models.CharField('Miembro inferior izquierdo | Aparentes', max_length=10, blank=True)
    arm_r_mt = models.CharField('Brazo derecho | TM', max_length=10, blank=True)
    arm_l_mt = models.CharField('Brazo izquierdo | TM', max_length=10, blank=True)
    forearm_r_mt = models.CharField('Antebrazo derecho | TM', max_length=10, blank=True)
    forearm_l_mt = models.CharField('Antebrazo izquierdo | TM', max_length=10, blank=True)
    thigh_r_mt = models.CharField('Muslo derecho | TM', max_length=10, blank=True)
    thigh_l_mt = models.CharField('Muslo izquierdo | TM', max_length=10, blank=True)
    leg_r_mt = models.CharField('Pierna derecha | TM', max_length=10, blank=True)
    leg_l_mt = models.CharField('Pierna izquierda | TM', max_length=10, blank=True)

    def __str__(self):
        if hasattr(self, 'athlete'):
            return f'{self.athlete.user.first_name} {self.athlete.user.last_name}'
        else:
            return self.zone