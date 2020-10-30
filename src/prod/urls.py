from django.urls import path
from .views import ProductView, ImageView


app_name = "prod"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('prod/', ProductView.as_view()),
    path('prod/<int:pk>', ProductView.as_view()),
    path('prod/images/', ImageView.as_view()),
    path('prod/images/<int:pk>', ImageView.as_view()),
]
