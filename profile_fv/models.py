from django.db import models

#Models
from users.models import Athlete

class Profile_fv(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='profile_fv')
    weight = models.FloatField('Peso', null=True, blank=True)
    speed1 = models.FloatField('Velocidad 1', null=True, blank=True)
    speed2 = models.FloatField('Velocidad 2', null=True, blank=True)
    speed3 = models.FloatField('Velocidad 3', null=True, blank=True)
    speed4 = models.FloatField('Velocidad 4', null=True, blank=True)