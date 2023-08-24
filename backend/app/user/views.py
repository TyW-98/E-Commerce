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
        elif user.is_authenticated:
            requested_user_id = self.kwargs.get("pk")
            if requested_user_id == str(user.id):
                return get_user_model().objects.filter(id=user.id)
            else: 
                raise PermissionDenied("You do not have permission!")
        else:
            raise PermissionDenied("You do not have permission to this method")
    
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
        
        if not request.user.is_staff:
            raise PermissionDenied("You do not have permission to create a staff!")
        
        staff = get_user_model().objects.create_staff(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(methods=["post"], detail=False, permission_classes=[IsAdminUser], authentication_classes=[TokenAuthentication])
    def create_superuser(self,request, **kwargs):
        """Only Admin can create another admin account"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to create a superuser!")
        
        superuser = get_user_model().objects.create_superuser(
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            dob=serializer.validated_data["dob"],
            country=serializer.validated_data["country"],
            # ... any other fields you have
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)