from .models import Product, Images
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, ImagesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImagesSerializer