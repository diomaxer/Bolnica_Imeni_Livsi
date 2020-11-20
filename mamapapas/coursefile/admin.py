from django.contrib import admin
from .models import Coursefile


class CustomCoursefileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'coursefile', 'coursefile_order')}),
    )  
    list_display = ('title', 'coursefile', 'coursefile_order')

admin.site.register(Coursefile, CustomCoursefileAdmin)
