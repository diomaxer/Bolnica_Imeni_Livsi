from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserSerializer
from .forms import CustomUserCreationForm, UserForm

class UsersView(APIView):
    def get(self, request):
        articles = CustomUser.objects.all()
        serializer = CustomUserSerializer(articles, many=True)
        return Response({"User": serializer.data})

    def post(self, request):
        article = request.data.get("User")
        # Create an article from the above data
        serializer = CustomUserSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
           image_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(image_saved.username)})

    def put(self, request, pk):
        saved_article = get_object_or_404(CustomUser.objects.all(), pk=pk)
        data = request.data.get('User')
        serializer = CustomUserSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            image_saved = serializer.save()

        return Response({
            "success": "User '{}' updated successfully".format(image_saved.username)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(CustomUser.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "User with id `{}` has been deleted.".format(pk)
        }, status=204)


'''class SignUp(generic.CreateView):
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
'''