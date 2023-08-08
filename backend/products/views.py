from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .test_products import products_data


# Create your views here.
# Get Routes
class GetRoutesView(APIView):
    def get(self,request): 
        return Response("Test Home Connection")
    
# Get all products
class GetProductsView(APIView):
    def get(self,request):
        return Response(products_data)
    
# Get one product
class GetProductView(APIView):
    def get(self,request, pk):
        product = None
        for prod in products_data: 
            if prod["id"] == pk:
                product = prod 
                break
            
        if product: 
            return Response(product)
        else: 
            return Response({"Error": "Product not found"}, status=404)
        