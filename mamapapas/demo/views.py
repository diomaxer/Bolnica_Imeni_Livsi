from django.shortcuts import render

# Create your views here.
from demo.models import Demo

def demo_view(request, order, *args, **kwargs):
    pages = Demo.objects.filter().order_by('order')
    obj = Demo.objects.get(order=order)
    pagenumber = Demo.objects.get(order=order).order
    increment = order + 1
    decrement = order - 1

    my_context = {
        'pagenumber' : pagenumber,
        'increment' : increment,
        'decrement' : decrement,
        'obj' : obj,
        'pages' : pages,
    }

    return render(request, 'courses/demo.html', my_context)