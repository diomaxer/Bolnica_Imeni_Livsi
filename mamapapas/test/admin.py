from django.contrib import admin
from .models import Test

class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')

admin.site.register(Test, TestAdmin)
