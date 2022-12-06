from django.contrib import admin

from .models import Fat_rate

@admin.register(Fat_rate)
class FatAdmin(admin.ModelAdmin):
    pass
