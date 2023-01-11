from django.db import models

from accounts.models import CustomUser


class Website(models.Model):
    url = models.URLField()
    authorization = models.TextField(null=True, default=None)


class UpTime(models.Model):
    website = models.ForeignKey(to=Website, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)


class DownTime(models.Model):
    website = models.ForeignKey(to=Website, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)


class EmailDetails(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
