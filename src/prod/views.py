from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.
def all_view(request, *args, **kwargs):
    return render(request, 'all.html', {})

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'create_product.html', context)