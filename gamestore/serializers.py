from rest_framework import serializers

from gamestore.models import Product, ProductList, User


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=255)
    class Meta:
        fields = ('name', 'description', 'price')


class ProductListSerializer(serializers.Serializer):
    class Meta:
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

