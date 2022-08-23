from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Athlete, User

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('user', 'manager', 'birthdate', 'gender', 'age', 'created', 'modified')}),
    )

    readonly_fields = ('created', 'modified')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email',)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'phone', 'password')}),
        ('Role', {'fields': ('role',)}),
    )
    