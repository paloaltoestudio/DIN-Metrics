from django.contrib import admin

#Models
from .models import Bilateral

@admin.register(Bilateral)
class BilateralAdmin(admin.ModelAdmin):
    pass
