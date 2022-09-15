from django.db import models

#models
from users.models import Athlete

class SJ(models.Model):
    #athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='SJ')
    month1 = models.FloatField('Mes 1', null=True, blank=True)
    month2 = models.FloatField('Mes 2', null=True, blank=True)
    month3 = models.FloatField('Mes 3', null=True, blank=True)
    month4 = models.FloatField('Mes 4', null=True, blank=True)
    month5 = models.FloatField('Mes 5', null=True, blank=True)
    month6 = models.FloatField('Mes 6', null=True, blank=True)
    month7 = models.FloatField('Mes 7', null=True, blank=True)
    month8 = models.FloatField('Mes 8', null=True, blank=True)
    month9 = models.FloatField('Mes 9', null=True, blank=True)
    month10 = models.FloatField('Mes 10', null=True, blank=True)
    month11 = models.FloatField('Mes 11', null=True, blank=True)
    month12 = models.FloatField('Mes 12', null=True, blank=True)
    

class CMJ(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='CMJ')
    month1 = models.FloatField('Mes 1', null=True, blank=True)
    month2 = models.FloatField('Mes 2', null=True, blank=True)
    month3 = models.FloatField('Mes 3', null=True, blank=True)
    month4 = models.FloatField('Mes 4', null=True, blank=True)
    month5 = models.FloatField('Mes 5', null=True, blank=True)
    month6 = models.FloatField('Mes 6', null=True, blank=True)
    month7 = models.FloatField('Mes 7', null=True, blank=True)
    month8 = models.FloatField('Mes 8', null=True, blank=True)
    month9 = models.FloatField('Mes 9', null=True, blank=True)
    month10 = models.FloatField('Mes 10', null=True, blank=True)
    month11 = models.FloatField('Mes 11', null=True, blank=True)
    month12 = models.FloatField('Mes 12', null=True, blank=True)
    

class DROPS(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='DROPS')
    month1 = models.FloatField('Mes 1', null=True, blank=True)
    month2 = models.FloatField('Mes 2', null=True, blank=True)
    month3 = models.FloatField('Mes 3', null=True, blank=True)
    month4 = models.FloatField('Mes 4', null=True, blank=True)
    month5 = models.FloatField('Mes 5', null=True, blank=True)
    month6 = models.FloatField('Mes 6', null=True, blank=True)
    month7 = models.FloatField('Mes 7', null=True, blank=True)
    month8 = models.FloatField('Mes 8', null=True, blank=True)
    month9 = models.FloatField('Mes 9', null=True, blank=True)
    month10 = models.FloatField('Mes 10', null=True, blank=True)
    month11 = models.FloatField('Mes 11', null=True, blank=True)
    month12 = models.FloatField('Mes 12', null=True, blank=True)
    

class Q(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True, related_name='Q')
    month1 = models.FloatField('Mes 1', null=True, blank=True)
    month2 = models.FloatField('Mes 2', null=True, blank=True)
    month3 = models.FloatField('Mes 3', null=True, blank=True)
    month4 = models.FloatField('Mes 4', null=True, blank=True)
    month5 = models.FloatField('Mes 5', null=True, blank=True)
    month6 = models.FloatField('Mes 6', null=True, blank=True)
    month7 = models.FloatField('Mes 7', null=True, blank=True)
    month8 = models.FloatField('Mes 8', null=True, blank=True)
    month9 = models.FloatField('Mes 9', null=True, blank=True)
    month10 = models.FloatField('Mes 10', null=True, blank=True)
    month11 = models.FloatField('Mes 11', null=True, blank=True)
    month12 = models.FloatField('Mes 12', null=True, blank=True)

