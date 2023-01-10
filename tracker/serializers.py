from rest_framework import serializers

from tracker.models import EmailDetails, Website


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = EmailDetails
        fields = ("email",)


class WebsiteSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    authorization = serializers.CharField(default=None)

    class Meta:
        model = Website
        fields = ("url", "authorization")
