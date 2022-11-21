from django.contrib import admin

#Models
from .models import FV, FV_register, FV_observation

class FVInline(admin.TabularInline):
    model = FV_register

@admin.register(FV)
class Profile_fvAdmin(admin.ModelAdmin):
    inlines = [FVInline,]


@admin.register(FV_register)
class FV_registerAdmin(admin.ModelAdmin):
    pass


@admin.register(FV_observation)
class FV_observationAdmin(admin.ModelAdmin):
    pass

