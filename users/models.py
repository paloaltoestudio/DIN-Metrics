
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        print('--------------username: ', user.username, user.email)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Modify default User class to include additional information
    
    For example: roles.
    """

    objects = UserManager()

    ROLE_CHOICES = (
          ('ADMIN', 'Admin'),
          ('MANAGER', 'Manager'),
          ('ATHLETE', 'Athlete'),
      )
    username = None
    email = models.EmailField('email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    role = models.CharField('Rol', max_length=20, choices=ROLE_CHOICES, default='MANAGER')

    first_name = models.CharField(("first name"), max_length=150, blank=False)
    last_name = models.CharField(("last name"), max_length=150, blank=False)
    phone = models.CharField('Teléfono', max_length=11, blank=True, null=True)
    document = models.BigIntegerField('Cédula', null=True, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Athlete(models.Model):
    """Class for Athlete profile, extending User model"""
    
    GENDER_CHOICES = (
        ('', ''),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete')
    birthdate = models.DateField('Fecha de Nacimiento',blank=True, null=True)
    gender = models.CharField('Género', max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField('Edad', blank=True, null=True)
    team = models.CharField('Equipo', max_length=30, blank=True, null=True)
    sport = models.CharField('Deporte', max_length=30, blank=True, null=True)
    size = models.CharField('Talla', max_length=10, blank=True, null=True)
    weight = models.CharField('Peso', max_length=6, blank=True, null=True)
    eps = models.CharField('EPS', max_length=30, blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='Athlete', blank=True, null=True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    modified = models.DateTimeField('Fecha de modificación', auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



