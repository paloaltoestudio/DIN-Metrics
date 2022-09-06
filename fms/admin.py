from django.contrib import admin
from .models import Fms

@admin.register(Fms)
class FmsAdmin(admin.ModelAdmin):
    pass
