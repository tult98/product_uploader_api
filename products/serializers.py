from rest_framework import serializers
from products.models import (
    Product,
    Image,
)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
