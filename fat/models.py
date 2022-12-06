from django.db import models

#Models
from users.models import Athlete

class Fat_rate(models.Model):
    date = models.DateField(blank=True)
    is_athlete = models.BooleanField('Es deportista', blank=True)
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    triceps = models.FloatField('Triceps', blank=True)
    subscap = models.FloatField('Subescapular', blank=True)
    abdominal = models.FloatField('Abdominal', blank=True)
    suprailiac = models.FloatField('Suprailiaco', blank=True)
    thigh = models.FloatField('Muslo', blank=True)
    calf = models.FloatField('Pantorrilla', blank=True)
    fat_rate = models.FloatField('Porcentaje de grasa', blank=True)
