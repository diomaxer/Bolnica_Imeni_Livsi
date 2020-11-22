from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request):
    if request.method == 'POST':
    else:
        form = AuthenticationForm()
    return render(request, 'account/login')