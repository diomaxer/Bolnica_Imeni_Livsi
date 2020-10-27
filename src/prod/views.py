from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

from .models import Images
from .forms import ProductForm, ImageForm
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import OrderSerializer

# Create your views here.
def all_view(request, *args, **kwargs):
    return render(request, 'all.html', {})

class OrderView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = OrderSerializer


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

@login_required
def post(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=2)

    if request.method == 'POST':

        postForm = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = ProductForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        context = {'postForm': postForm, 'formset': formset}
    return render(request, 'create_product.html', context)


'''from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.
def all_view(request, *args, **kwargs):
    return render(request, 'all.html', {})

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'create_product.html', context)'''