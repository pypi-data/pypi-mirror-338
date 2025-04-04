from django.dispatch import receiver
from pretix.presale.signals import html_head
from django.utils.safestring import mark_safe
from django import forms
import requests
import secrets
from pretix.base.signals import order_placed, register_global_settings

# Code in <head> injizieren
@receiver(html_head, dispatch_uid="custom_head_html")
def inject_head_code(sender, request, **kwargs):
    event = sender
    custom_code = event.settings.get("custom_head_code")

    if custom_code:
        return str('\n' + custom_code)
    return ""

# Ticket-Kauf tracken
@receiver(order_placed)
def track_order(sender, order, **kwargs):
    event = sender
    plausible_url = event.settings.get("plausible_url")
    plausible_domain = event.settings.get("plausible_domain")

    if plausible_url and plausible_domain:
        payload = {
            "name": "Ticket Purchase",
            "url": f"https://{plausible_domain}/{event.event.organizer.slug}/{event.event.slug}/checkout",
            "domain": plausible_domain,
            "revenue": {
                "amount": str(order.total),
                "currency": event.event.currency
            }
        }
        try:
            requests.post(f"{plausible_url}/api/event", json=payload, timeout=3)
        except requests.exceptions.RequestException as e:
            print(f"Plausible Tracking Error: {e}")

@receiver(register_global_settings, dispatch_uid="pretix_custom_head_global_settings")
def register_global_settings(sender, **kwargs):
    return {
        "custom_head_code": forms.CharField(
            widget=forms.Textarea,
            required=False,
            label="Custom Head Code"
        ),
        "plausible_url": forms.URLField(
            required=False,
            label="Plausible Analytics URL"
        ),
        "plausible_domain": forms.CharField(
            required=False,
            label="Plausible Analytics Domain"
        ),
    }