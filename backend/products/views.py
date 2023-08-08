from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from .test_products import products_data


# Create your views here.
# Get Routes
class GetRoutesView(APIView):
    def get(self,request): 
        return Response("Test Home Connection")
    
# Get all products
class GetProductsView(APIView):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    
    def get(self,request, *args, **kwargs):
        return Response(self.serializer.data)
    
# Get one product
class GetProductView(APIView):
    def get(self,request, pk):
        try: 
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"Error": "Product not found"}, status=404)