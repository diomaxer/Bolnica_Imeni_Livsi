from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, UsersPromocode


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'email', 'permissions', 'lessons_completed', 'phone', 'password', 'promo')}),
    )  
    list_display = ('date_joined', 'username', 'first_name', 'email', 'phone', 'last_login', 'promo')


admin.site.register(User, CustomUserAdmin)
admin.site.register(UsersPromocode)
admin.site.unregister(Group)

