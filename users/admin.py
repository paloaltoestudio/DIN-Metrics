from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Athlete, User


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('user', 'phone', 'birthdate', 'gender', 'age', 'created', 'modified')}),
    )

    readonly_fields = ('created', 'modified')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email')}),
        ('Role', {'fields': ('role',)}),
    )
    