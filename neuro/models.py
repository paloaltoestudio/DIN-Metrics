from django.db import models

#models
from users.models import Athlete

class SJ(models.Model):
    #athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='SJ')
    month1 = models.FloatField('Mes 1', blank=True)
    month2 = models.FloatField('Mes 2', blank=True)
    month3 = models.FloatField('Mes 3', blank=True)
    month4 = models.FloatField('Mes 4', blank=True)
    month5 = models.FloatField('Mes 5', blank=True)
    month6 = models.FloatField('Mes 6', blank=True)
    month7 = models.FloatField('Mes 7', blank=True)
    month8 = models.FloatField('Mes 8', blank=True)
    month9 = models.FloatField('Mes 9', blank=True)
    month10 = models.FloatField('Mes 10', blank=True)
    month11 = models.FloatField('Mes 11', blank=True)
    month12 = models.FloatField('Mes 12', blank=True)
    

class CMJ(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='CMJ')
    month1 = models.FloatField('Mes 1', blank=True)
    month2 = models.FloatField('Mes 2', blank=True)
    month3 = models.FloatField('Mes 3', blank=True)
    month4 = models.FloatField('Mes 4', blank=True)
    month5 = models.FloatField('Mes 5', blank=True)
    month6 = models.FloatField('Mes 6', blank=True)
    month7 = models.FloatField('Mes 7', blank=True)
    month8 = models.FloatField('Mes 8', blank=True)
    month9 = models.FloatField('Mes 9', blank=True)
    month10 = models.FloatField('Mes 10', blank=True)
    month11 = models.FloatField('Mes 11', blank=True)
    month12 = models.FloatField('Mes 12', blank=True)
    

class DROPS(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='DROPS')
    month1 = models.FloatField('Mes 1', blank=True)
    month2 = models.FloatField('Mes 2', blank=True)
    month3 = models.FloatField('Mes 3', blank=True)
    month4 = models.FloatField('Mes 4', blank=True)
    month5 = models.FloatField('Mes 5', blank=True)
    month6 = models.FloatField('Mes 6', blank=True)
    month7 = models.FloatField('Mes 7', blank=True)
    month8 = models.FloatField('Mes 8', blank=True)
    month9 = models.FloatField('Mes 9', blank=True)
    month10 = models.FloatField('Mes 10', blank=True)
    month11 = models.FloatField('Mes 11', blank=True)
    month12 = models.FloatField('Mes 12', blank=True)
    

class Q(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='Q')
    month1 = models.FloatField('Mes 1', blank=True)
    month2 = models.FloatField('Mes 2', blank=True)
    month3 = models.FloatField('Mes 3', blank=True)
    month4 = models.FloatField('Mes 4', blank=True)
    month5 = models.FloatField('Mes 5', blank=True)
    month6 = models.FloatField('Mes 6', blank=True)
    month7 = models.FloatField('Mes 7', blank=True)
    month8 = models.FloatField('Mes 8', blank=True)
    month9 = models.FloatField('Mes 9', blank=True)
    month10 = models.FloatField('Mes 10', blank=True)
    month11 = models.FloatField('Mes 11', blank=True)
    month12 = models.FloatField('Mes 12', blank=True)


