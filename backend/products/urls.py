from django.urls import path

from .views import GetProductsView, GetProductView, GetRoutesView

urlpatterns = [
    path("", GetRoutesView.as_view(), name="Home Route"),
    path("products/", GetProductsView.as_view(), name="Products Route"),
    path("products/<int:pk>/", GetProductView.as_view(), name="Product Route")
]