from django.db import models

#Models
from users.models import Athlete

class Fms(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='fms')
    date = models.DateField(blank=True, null=True)
    squat_score = models.IntegerField('Sentadilla | Puntuación Parcial', blank=True, null=True, default=0)
    squat_observations = models.TextField('Sentadilla | Observaciones', blank=True, null=True, default='')
    fence_step_l_score = models.IntegerField('Paso Izquierda | Puntuación Parcial', blank=True, null=True, default=0)
    fence_step_r_score = models.IntegerField('Paso Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    fence_step_observations = models.TextField('Paso | Observaciones', blank=True, null=True, default='')
    lunge_l_score = models.IntegerField('Estocada Izquierda | Puntuación Parcial', blank=True, null=True, default=0)
    lunge_r_score = models.IntegerField('Estocada Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    lunge_observations = models.TextField('Estocada | Observaciones', blank=True, null=True, default='')
    shoulder_l_score = models.IntegerField('Movilidad de hombros Izquierda | Puntuación Parcial', blank=True, null=True, default=0)
    shoulder_r_score = models.IntegerField('Movilidad de hombros Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    shoulder_observations = models.TextField('Movilidad de hombros | Observaciones', blank=True, null=True, default='')
    leg_raise_l_score = models.IntegerField('Elevación Pierna Izquirda | Puntuación Parcial', blank=True, null=True, default=0)
    leg_raise_r_score = models.IntegerField('Elevación Pierna Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    leg_raise_observations = models.TextField('Elevación Pierna | Observaciones', blank=True, null=True, default='')
    trunk_l_score = models.IntegerField('Estabilidad Tronco Flexion Izquirda | Puntuación Parcial', blank=True, null=True, default=0)
    trunk_r_score = models.IntegerField('Estabilidad Tronco Flexion Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    trunk_observations = models.TextField('Estabilidad Tronco Flexion | Observaciones', blank=True, null=True, default='')
    trunk_rot_l_score = models.IntegerField('Estabilidad Tronco Rotación Izquirda | Puntuación Parcial', blank=True, null=True, default=0)
    trunk_rot_r_score = models.IntegerField('Estabilidad Tronco Rotación Derecha | Puntuación Parcial', blank=True, null=True, default=0)
    trunk_rot_observations = models.TextField('Estabilidad Tronco Rotación | Observaciones', blank=True, null=True, default='')
    total = models.IntegerField('Puntuación Total', blank=True, null=True, default=0)

    def __str__(self):
        return f'{self.date} - {self.athlete.user.first_name}'
