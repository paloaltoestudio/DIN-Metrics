from unicodedata import name
from django.db import models

#models
from users.models import Athlete

class NeuroBase(models.Model):
    date = models.DateField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

class SJ(NeuroBase):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='SJ')

    def __str__(self):
        return 'SJ'
    

class CMJ(NeuroBase):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='CMJ')

    def __str__(self):
        return 'CMJ'
    

class DROPS(NeuroBase):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='DROPS')

    def __str__(self):
        return 'DROPS'
    

class Q(NeuroBase):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='Q')

    def __str__(self):
        return 'Q'

