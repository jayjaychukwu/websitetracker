import requests
from celery import shared_task

from .models import DownTime, UpTime, Website
