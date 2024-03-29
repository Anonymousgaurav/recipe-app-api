from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

""" Django admin customiztaion"""

from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)

# Register your models here.
