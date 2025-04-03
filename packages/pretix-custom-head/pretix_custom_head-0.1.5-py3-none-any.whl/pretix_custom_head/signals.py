from django.dispatch import receiver
from pretix.presale.signals import html_head
from django.utils.safestring import mark_safe
import requests
from pretix.base.signals import order_placed

# Code in <head> injizieren
@receiver(html_head)
def inject_head_code(sender, request, **kwargs):
    event = sender
    custom_code = event.settings.get("custom_head_code")

    if custom_code:
        return mark_safe(custom_code)
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
            "url": f"https://{plausible_domain}/checkout",
            "domain": plausible_domain,
            "props": {
                "order_code": order.code,
                "value": str(order.total),
                "currency": order.currency
            }
        }
        try:
            requests.post(f"{plausible_url}/api/event", json=payload, timeout=3)
        except requests.exceptions.RequestException as e:
            print(f"Plausible Tracking Error: {e}")