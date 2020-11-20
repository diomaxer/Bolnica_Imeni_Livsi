from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewPromoForm
from promocode.models import Promo


"""
    def login_view(request):
    if request.method == 'POST':
    else:
        form = AuthenticationForm()
    return render(request, 'account/login')
"""

def new_promo_view(request):
    try:
        all_promo = len(Promo.objects.all())
        if request.method == 'POST':

            postForm = NewPromoForm(request.POST)

            if postForm.is_valid():
                post_form = postForm.save(commit=False)
                post_form.user = request.user
                for i in range(all_promo):
                    if post_form.new_promo == Promo.objects.all()[i].name:
                        post_form.save()
                        return HttpResponseRedirect("/")
                return HttpResponseRedirect("/")
            else:
                print(postForm.errors)
        else:
            postForm = NewPromoForm()
            context = {'postForm': postForm}
        return render(request, 'promocode/new_promo.html', context)
    except ValueError:
        return HttpResponseRedirect("/")
