"""
Views for custom user API
"""
from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated
from rest_framework.response import Response
from user.serializers import UserSerializer


class IsOwnerAdminOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj
            or request.user.is_admin
            or request.user.is_staff
        )

class UserViewSets(viewsets.ModelViewSet):
    """View for User API"""
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return get_user_model().objects.filter(id=user.pk)
        return get_user_model().objects.none()
    
    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def create_user(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)