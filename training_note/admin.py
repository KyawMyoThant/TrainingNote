from curses.ascii import US
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Title, Task, User
# Register Title


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Status', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'is_teacher', 'password1', 'password2')}
         ),
    )


admin.site.register(Title)
admin.site.register(Task)
admin.site.register(User, CustomUserAdmin)
