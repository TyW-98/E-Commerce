"""
Custom User serialzier
"""
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _  # noqa
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "dob",
            "country"
        ]
        extra_kwargs = {"password": {"write_only": True, "min_length": 7}}

    def create(self, validated_data):
        """Create and return user model"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update user details"""
        password = validated_data.pop("password", None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
    
class AuthTokenSerializer(serializers.Serializer):
    """Token Serializer"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )
    
    def validate(self, attrs):
        """Validate and authenticate User"""
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password
        )
        
        if not user:
            msg = _(
                "Unable to authenticate with the provided credentials"
            )
            raise serializers.ValidationError(msg, code="authorization")
        
        attrs["user"] = user
        return attrs
        
    
    
    