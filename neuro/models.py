from unicodedata import name
from django.db import models

#models
from users.models import Athlete

class SJ(models.Model):
    #athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='SJ')
    date = models.DateField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'SJ'
    

class CMJ(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='CMJ')
    date = models.DateField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'CMJ'
    

class DROPS(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='DROPS')
    date = models.DateField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'DROPS'
    

class Q(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='Q')
    date = models.DateField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Q'

