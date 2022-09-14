from django.contrib import admin

#models
from .models import SJ, CMJ, DROPS, Q

@admin.register(SJ)
class SJAdmin(admin.ModelAdmin):
    pass

@admin.register(CMJ)
class CMJAdmin(admin.ModelAdmin):
    pass

@admin.register(DROPS)
class DROPSAdmin(admin.ModelAdmin):
    pass

@admin.register(Q)
class QAdmin(admin.ModelAdmin):
    pass

