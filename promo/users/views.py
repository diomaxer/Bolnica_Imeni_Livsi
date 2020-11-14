from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from .forms import CustomUserCreationForm, UserForm


def home_view(request):
    return render(request, 'home.html', {})


class SignUp(generic.CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'


def signup_view(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)