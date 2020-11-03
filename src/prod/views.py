from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

from .models import Images, Product
from .forms import ProductForm, ImageForm
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


# Create your views here.
def all_view(request, *args, **kwargs):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'all.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'watch/detail_view.html'
    context_object_name = 'prod'


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


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
