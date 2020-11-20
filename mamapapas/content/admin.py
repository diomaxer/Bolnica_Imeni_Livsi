from django.contrib import admin

# Register your models here.
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ('course','lesson', 'content','order',)

admin.site.register(Content, ContentAdmin)