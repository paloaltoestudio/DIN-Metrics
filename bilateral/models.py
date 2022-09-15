from django.db import models

#Models
from users.models import Athlete

class Bilateral(models.Model):

    JUMP_CHOICES = (
        ('SJ', 'SJ'),
        ('CMJ', 'CMJ'),
        ('DROPS', 'DROPS'),
        ('Q', 'Q'),
    )

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='bilateral')
    date = models.DateField('Fecha', null=True, blank=True)
    jump = models.CharField('Salto', max_length=5, choices=JUMP_CHOICES, null=True, blank=True)
    left = models.FloatField('Izquierda', null=True, blank=True)
    right = models.FloatField('Derecha', null=True, blank=True)
    deficit = models.FloatField('Déficit', null=True, blank=True)

