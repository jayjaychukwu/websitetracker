from django.urls import path

from .views import NotificationEmailAPIView, WebsitesToMonitorAPIView

urlpatterns = [
    path("email/", NotificationEmailAPIView.as_view(), name="notification_email"),
    path("website/", WebsitesToMonitorAPIView.as_view(), name="website"),
]
