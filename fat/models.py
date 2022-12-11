from django.db import models

#Models
from users.models import Athlete

class Fat_rate(models.Model):
    date = models.DateField(blank=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='fats')
    triceps = models.FloatField('Triceps', blank=True)
    subscap = models.FloatField('Subescapular', blank=True)
    abdominal = models.FloatField('Abdominal', blank=True)
    suprailiac = models.FloatField('Suprailiaco', blank=True)
    thigh = models.FloatField('Muslo', blank=True)
    calf = models.FloatField('Pantorrilla', blank=True)
    fat_rate = models.FloatField('Porcentaje de grasa', blank=True, null=True)


class FatObservation(models.Model):

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='fat_observations')
    observation = models.CharField('Observaciones', max_length=200, blank=True, null=True)
