from rest_framework import serializers

from .models import CustomUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, min_length=2)
    password = serializers.CharField(max_length=30, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        return user
