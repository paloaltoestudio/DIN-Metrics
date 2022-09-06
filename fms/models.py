from django.db import models

#Models
from users.models import Athlete

class Fms(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    squat_score = models.FloatField('Sentadilla | Puntuación Parcial', blank=True, null=True)
    squat_observations = models.TextField('Sentadilla | Observaciones', blank=True, null=True)
    fence_step_l_score = models.FloatField('Paso Izquierda | Puntuación Parcial', blank=True, null=True)
    fence_step_l_observations = models.TextField('Paso Izquierda | Observaciones', blank=True, null=True)

    def __str__(self):
        return self.athlete.user.first_name

