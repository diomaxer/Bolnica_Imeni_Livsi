from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register('api/product', ProductViewSet, 'product')

urlpatterns = [
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail_view'),
]

urlpatterns = router.urls
