from django.db import models

#Models
from users.models import Athlete

class Fms(models.Model):

    TEST_CHOICES = (
        ('Sentadilla con brazos estirados', 'Sentadilla con brazos estirados'),
        ('Paso de valla', 'Paso de valla'),
        ('Paso de valla iz', 'Paso de valla Izquierda'),
        ('Paso de valla der', 'Paso de valla Derecha'),
        ('Estocada', 'Estocada'),
        ('Movilidad de hombros', 'Movilidad de hombros'),
        ('Elevación activa con la pierna recta', 'Elevación activa con la pierna recta'),
        ('Estabilidad de tronco en flexión', 'Estabilidad de tronco en flexión'),
        ('Estabilidad de tronco en rotación', 'Estabilidad de tronco en rotación'),
    )

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('Prueba', max_length=50, choices=TEST_CHOICES, blank=True)
    test_slug = models.SlugField('Slug', max_length=30, unique=True, blank=True)
    score = models.FloatField('Puntuación Parcial', blank=True)
    observations = models.TextField('Observaciones', blank=True)

    def __str__(self):
        return self.test_slug
