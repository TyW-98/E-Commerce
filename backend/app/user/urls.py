"""
URL mapping for user API
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register("user", views.UserViewSets, basename="user")

app_name = "user"

urlpatterns = [
    path("", include(router.urls)),
    path("create_user/", views.UserViewSets.as_view({"post": "create_user"}), name="create-user"),
    path("account/", views.UserViewSets.as_view({"get": "fetch_user_details"}), name="fetch-user-details")
]
