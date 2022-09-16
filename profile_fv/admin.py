from django.contrib import admin

#Models
from .models import Profile_fv

@admin.register(Profile_fv)
class Profile_fvAdmin(admin.ModelAdmin):
    pass

