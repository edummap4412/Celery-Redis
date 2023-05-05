import jwt
from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics

from gamestore.models import Product
from gamestore.serializers import ProductSerializer


class ProductList(generics.ListAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        products = Product.objects.all()
        return products

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Product.objects.create(
                name=request.data.get('name'),
                price=request.data.get('price'),
                description=request.data.get('description')

            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        products_delete = Product.objects.all()
        products_delete.delete()

        return Response(data={'destroy': 'Tudo deletado'}, status=status.HTTP_200_OK)


class ProductDetail(generics.ListAPIView, generics.UpdateAPIView, generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            return Product.objects.all()
        except :
            raise Exception(Http404)

    def update(self, request, *args, **kwargs):
        product = Product.objects.filter(pk=kwargs.get('pk')).first()
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs.get('pk'))
            product.delete()
        except Product.DoesNotExist:
            raise Http404
        return Response(status=status.HTTP_204_NO_CONTENT)
