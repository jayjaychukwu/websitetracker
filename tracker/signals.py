from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Website
from .tasks import check_website_status


@receiver(post_save, sender=Website)
def check_website_status_on_create(sender, instance, created, **kwargs):
    if created:
        check_website_status.delay(instance.id)
