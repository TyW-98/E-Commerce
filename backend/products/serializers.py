from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Order, OrderedItem, Product, Review, ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()

    class Meta: 
        model = Product
        fields = "__all__"
        
    def get_average_rating(self, obj):
        return obj.average_rating()
    
    def get_discounted_price(self,obj):
        return obj.calculate_discounted_price()