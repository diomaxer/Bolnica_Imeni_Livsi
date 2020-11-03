from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail_view'),
]