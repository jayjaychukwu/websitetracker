from django.db import models


class Website(models.Model):
    url = models.URLField()
    authorization = models.TextField()


class UpTime(models.Model):
    website = models.ForeignKey(to=Website, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    duration = models.DurationField()


class DownTime(models.Model):
    website = models.ForeignKey(to=Website, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    reason = models.TextField(null=True)
