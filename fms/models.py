from django.db import models

#Models
from users.models import Athlete

class Fms(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    squat_score = models.FloatField('Sentadilla | Puntuación Parcial', blank=True, null=True)
    squat_observations = models.TextField('Sentadilla | Observaciones', blank=True, null=True)
    fence_step_l_score = models.FloatField('Paso Izquierda | Puntuación Parcial', blank=True, null=True)
    fence_step_r_score = models.FloatField('Paso Derecha | Puntuación Parcial', blank=True, null=True)
    fence_step_observations = models.TextField('Paso | Observaciones', blank=True, null=True)
    lunge_l_score = models.FloatField('Estocada Izquierda | Puntuación Parcial', blank=True, null=True)
    lunge_r_score = models.FloatField('Estocada Derecha | Puntuación Parcial', blank=True, null=True)
    lunge_observations = models.TextField('Estocada | Observaciones', blank=True, null=True)
    shoulder_l_score = models.FloatField('Movilidad de hombros Izquierda | Puntuación Parcial', blank=True, null=True)
    shoulder_r_score = models.FloatField('Movilidad de hombros Derecha | Puntuación Parcial', blank=True, null=True)
    shoulder_observations = models.TextField('Movilidad de hombros | Observaciones', blank=True, null=True)
    leg_raise_l_score = models.FloatField('Elevación Pierna Izquirda | Puntuación Parcial', blank=True, null=True)
    leg_raise_r_score = models.FloatField('Elevación Pierna Derecha | Puntuación Parcial', blank=True, null=True)
    leg_raise_observations = models.TextField('Elevación Pierna | Observaciones', blank=True, null=True)
    trunk_l_score = models.FloatField('Estabilidad Tronco Flexion Izquirda | Puntuación Parcial', blank=True, null=True)
    trunk_r_score = models.FloatField('Estabilidad Tronco Flexion Derecha | Puntuación Parcial', blank=True, null=True)
    trunk_observations = models.TextField('Estabilidad Tronco Flexion | Observaciones', blank=True, null=True)
    trunk_rot_l_score = models.FloatField('Estabilidad Tronco Rotación Izquirda | Puntuación Parcial', blank=True, null=True)
    trunk_rot_r_score = models.FloatField('Estabilidad Tronco Rotación Derecha | Puntuación Parcial', blank=True, null=True)
    trunk_rot_observations = models.TextField('Estabilidad Tronco Rotación | Observaciones', blank=True, null=True)
    total = models.FloatField('Puntuación Total', blank=True, null=True)

    def __str__(self):
        return self.athlete.user.first_name

