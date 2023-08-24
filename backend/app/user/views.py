"""
Views for custom user API
"""
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    BasePermission,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response
from user.serializers import UserSerializer


class IsAdminOrStaff(BasePermission):
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
        if user.is_staff or user.is_superuser:
            return get_user_model().objects.all() 
        else:
            raise PermissionDenied("You do not have permission to access this resource")
        
    @action(methods=["get"], detail=False, permission_classes=[IsAuthenticated], authentication_classes=[TokenAuthentication])
    def fetch_user_details(self,request):
        user_details = get_user_model().objects.get(id=self.request.user.id)
        serializer = UserSerializer(user_details, many=False)
        return Response(serializer.data)
    
    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def create_user(self, request, **kwargs):
        """AllowAny to create new account"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_model().objects.create_user(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=["post"], detail=False, permission_classes=[IsAdminOrStaff], authentication_classes = [TokenAuthentication])
    def create_staff(self,request, **kwargs):
        """Only Staff or admin can create another staff account"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = get_user_model().objects.create_staff(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=["post"], detail=False, permission_classes=[IsAdminUser], authentication_classes=[TokenAuthentication])
    def create_superuser(self,request, **kwargs):
        """Only Admin can create another admin account"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        superuser = get_user_model().objects.create_superuser(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)