from django.contrib import admin

from osteo.models import Osteo

@admin.register(Osteo)
class OsteoAdmin(admin.ModelAdmin):
    pass
