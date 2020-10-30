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
# from .serializers import OrderSerializer, ImagesSerializer

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Images
from .serializers import ProductSerializer, ImagesSerializer


class ProductView(APIView):
    def get(self, request):
        articles = Product.objects.all()
        serializer = ProductSerializer(articles, many=True)
        return Response({"prod": serializer.data})

    def post(self, request):
        article = request.data.get("prod")
        # Create an article from the above data
        serializer = ProductSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
           prod_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(prod_saved.id_number)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('prod')
        serializer = ProductSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            prod_saved = serializer.save()

        return Response({
            "success": "Product '{}' updated successfully".format(prod_saved.id_number)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Product.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)


class ImageView(APIView):
    def get(self, request):
        articles = Images.objects.all()
        serializer = ImagesSerializer(articles, many=True)
        return Response({"Image": serializer.data})

    def post(self, request):
        article = request.data.get("Image")
        # Create an article from the above data
        serializer = ImagesSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
           image_saved = serializer.save()
        return Response({"success": "Image '{}' created successfully".format(image_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Images.objects.all(), pk=pk)
        data = request.data.get('Image')
        serializer = ImagesSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            image_saved = serializer.save()

        return Response({
            "success": "Image '{}' updated successfully".format(image_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Images.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Image with id `{}` has been deleted.".format(pk)
        }, status=204)


def all_view(request, *args, **kwargs):
    return render(request, 'all.html', {})


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

"""

class OrderView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = OrderSerializer


class ImageView(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer





@login_required
def post(request):
    try:
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
    except KeyError:
        return HttpResponseRedirect("/")
        # return render(request, 'sucsess.html', {})
"""

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