from django.db import models

#Models
from users.models import Athlete

class FV(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='fv')
    date = models.DateField(blank=True)
    rm = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.date} - {self.athlete.user.first_name} {self.athlete.user.last_name}'


class FV_register(models.Model):
    profile_fv = models.ForeignKey(FV, on_delete=models.CASCADE, blank=True, null=True, related_name='fv_register')
    weight = models.FloatField('Peso', null=True, blank=True)
    speed1 = models.FloatField('Velocidad 1', null=True, blank=True)
    speed2 = models.FloatField('Velocidad 2', null=True, blank=True)
    speed3 = models.FloatField('Velocidad 3', null=True, blank=True)
    speed4 = models.FloatField('Velocidad 4', null=True, blank=True)