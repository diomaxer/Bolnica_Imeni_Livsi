from rest_framework.serializers import ModelSerializer
from .models import Product

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description']