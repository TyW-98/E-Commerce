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
    path("c-staff/", views.UserViewSets.as_view({"post": "create_staff"}), name="create-staff"),
    path("c-admin/", views.UserViewSets.as_view({"post": "create_superuser"}), name="create-admin"),
    path("account/", views.ManageUserView.as_view(), name="account")
]
