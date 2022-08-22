
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Modify default User class to include additional information
    
    For example: roles.
    """

    ROLE_CHOICES = (
          ('ADMIN', 'Admin'),
          ('MANAGER', 'Manager'),
          ('ATHLETE', 'Athlete'),
      )

    role = models.CharField('Rol', max_length=20, choices=ROLE_CHOICES, default='MANAGER')

    first_name = models.CharField(("first name"), max_length=150, blank=False)
    last_name = models.CharField(("last name"), max_length=150, blank=False)
    phone = models.CharField('Teléfono', max_length=11, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Athlete(models.Model):
    """Class for Athlete profile, extending User model"""
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthdate = models.DateField('Fecha de Nacimiento',blank=True, null=True)
    gender = models.CharField('Género', max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField('Edad', blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Athlete', null=True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    modified = models.DateTimeField('Fecha de modificación', auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



