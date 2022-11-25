

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ( 'phone', 'phone_verified')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        #    ('Custom info', {'fields': ('phone',)}),
    )


# admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)
