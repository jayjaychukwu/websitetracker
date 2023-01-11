import requests
from celery import shared_task
from celery.schedules import crontab
from django.utils import timezone

from afex.celery import app

from .models import DownTime, UpTime, Website


@shared_task
def check_website_status(website_ids):
    for website_id in website_ids:
        website = Website.objects.get(id=website_id)
    try:
        response = requests.get(website.url, headers=website.authorization)
        if response.status_code == 200:
            # website is up
            uptime = UpTime.objects.filter(website=website, end_time=None).first()
            if uptime:
                # website was already up, so do nothing
                pass
            else:
                # website has just come back up, so update the last downtime instance
                # and create a new uptime instance
                downtime = DownTime.objects.filter(website=website, end_time=None).first()
                if downtime:
                    downtime.end_time = timezone.now()
                    downtime.duration = downtime.end_time - downtime.start_time
                    downtime.save()
                UpTime.objects.create(website=website, start_time=timezone.now())
        else:
            # website is down
            downtime = DownTime.objects.filter(website=website, end_time=None).first()
            if downtime:
                # website was already down, so do nothing
                pass
            else:
                # website has just gone down, so update the last uptime instance
                # and create a new downtime instance
                uptime = UpTime.objects.filter(website=website, end_time=None).first()
                if uptime:
                    uptime.end_time = timezone.now()
                    uptime.duration = uptime.end_time - uptime.start_time
                    uptime.save()
                DownTime.objects.create(website=website, start_time=timezone.now(), reason=response.reason)
    except requests.RequestException as e:
        # website is down due to an error
        downtime = DownTime.objects.filter(website=website, end_time=None).first()
        if downtime:
            # website was already down, so do nothing
            pass
        else:
            # website has just gone down due to an error, so update the last uptime instance
            # and create a new downtime instance
            uptime = UpTime.objects.filter(website=website, end_time=None).first()
            if uptime:
                uptime.end_time = timezone.now()
                uptime.duration = uptime.end_time - uptime.start_time
                uptime.save()
            DownTime.objects.create(website=website, start_time=timezone.now(), reason=str(e))


@app.task
def check_all_websites_status():
    website_ids = list(Website.objects.values_list("id", flat=True))
    check_website_status.delay(website_ids)


app.conf.beat_schedule = {
    "check-all-websites-status": {
        "task": "tracker.tasks.check_all_websites_status",
        "schedule": 60.0,
    },
}
app.conf.timezone = "Africa/Lagos"
