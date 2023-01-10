import requests
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import EmailSerializer, WebsiteSerializer


class NotificationEmailAPIView(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        response = {
            "message": f"the email, {serializer.validated_data['email']}, has been added for notifications",
        }
        return Response(data=response)


class WebsitesToMonitorAPIView(GenericAPIView):
    serializer_class = WebsiteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "the website has been added for monitoring"})
