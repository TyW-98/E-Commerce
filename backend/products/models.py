from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    posterID = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, verbose_name="Seller ID")
    name = models.CharField(max_length=255, null=False, blank=False)
    brand = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null = False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    numReviews = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank = False, null=False)
    discount = models.DecimalField(max_digits = 4, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    stock = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.brand}"
    
class Review(models.Model):
    userID = models.ForeignKey(User, on_delete = models.CASCADE, null=False, verbose_name="User ID")
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, verbose_name="Product ID")
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False, blank=False)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.rating)
    
class Order(models.Model):
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, verbose_name="User ID")
    payment_method = models.CharField(max_length=50, null=False, blank=False)
    tax = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    delvieredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Created {str(self.createdAt)}"
    
class OrderedItem(models.Model): 
    order_id = models.ForeignKey(Order, verbose_name="Order ID", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name="Product ID", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name + f" qty: {self.quantity}"
    
class ShippingAddress(models.Model):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Order ID")
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{str(self.order_id)} {self.address}"

    
    