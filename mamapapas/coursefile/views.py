from django.shortcuts import render
from .models import Coursefile

def coursefile_view(request, *args, **kwargs):
    title = 'Файлы для скачивания'
    user = request.user

    if request.user.is_authenticated:
        coursefiles = Coursefile.objects.filter().order_by('coursefile_order') 
    else:
        coursefiles = 0

    my_context = {
        'title' : title,
        'coursefiles' : coursefiles,
    }
    
    return render(request, 'courses/course_files.html', my_context)
