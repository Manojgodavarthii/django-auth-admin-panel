from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        'id',
        'name',
        'mobile',
        'role',
        'is_active',
        'created_at'
    )

    ordering = ('id',)

    filter_horizontal = ()
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'mobile',
                    'password'
                )
            }
        ),
        (
            'Personal Information',
            {
                'fields': (
                    'name',
                    'role'
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
    )