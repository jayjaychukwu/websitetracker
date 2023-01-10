from rest_framework import serializers

from .models import CustomUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25)
    username = serializers.CharField(max_length=25)

    class Meta:
        model = CustomUser
        fields = ("username", "password")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                validated_data["username"], validated_data["email"], validated_data["password"]
            )

            return user
