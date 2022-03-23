from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.forms import CustomUserCreationForm, CustomUserChangeForm
from app.models import User, Status


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff'
    )
    list_filter = ('gender', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': (
            'phone_number', 'password',
            'first_name', 'last_name', 'country_code',
            'gender', 'birthdate', 'avatar', 'email'
        )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'phone_number', 'password1', 'password2', 'first_name',
                    'last_name', 'birthdate', 'email', 'is_staff', 'is_active'
                )
            }
        ),
    )
    search_fields = ('phone_number',)
    ordering = ('-id',)


admin.site.register(User, CustomUserAdmin)


@admin.register(Status)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'status']
