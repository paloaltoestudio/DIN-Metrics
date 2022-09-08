from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Athlete, User
from fms.models import Fms

class Fms_inline(admin.TabularInline):
    model = Fms

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {'fields': ('user', 'manager', 'birthdate', 'gender', 'age', 'created', 'modified')}),
        ('Información Básica', {'fields': ('team', 'sport', 'size', 'weight', 'eps')})
    )

    readonly_fields = ('created', 'modified')

    inlines = [
        Fms_inline,
    ]

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

    list_display = ('first_name', 'last_name', 'email',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),}),)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'document', 'email', 'phone')}),
        ('Role', {'fields': ('role',)}),
    )

    exclude = ['username',]
    