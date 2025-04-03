from django.db import models
from pretix.base.models import Event

class EventHeadTrackingSettings(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    custom_head_code = models.TextField(help_text="Hier kannst du beliebigen HTML/JS Code für den <head> einfügen.", blank=True)
    plausible_url = models.CharField(max_length=255, help_text="URL deiner selbst gehosteten Plausible Instanz", blank=True)
    plausible_domain = models.CharField(max_length=255, help_text="Tracking-Domain für Plausible", blank=True)