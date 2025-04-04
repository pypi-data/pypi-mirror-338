from django.dispatch import receiver
from pretix.presale.signals import html_head, process_response
from django.utils.safestring import mark_safe
from django import forms
import requests
import secrets
from pretix.base.signals import order_placed, register_global_settings
from pretix.base.middleware import _merge_csp, _parse_csp, _render_csp

# Code in <head> injizieren
@receiver(html_head, dispatch_uid="custom_head_html")
def inject_head_code(sender, request, **kwargs):
    event = sender
    custom_code = event.settings.get("custom_head_code")
    request.custom_code_nonce = secrets.token_urlsafe()
    custom_code = str(custom_code).replace('<script', f'<script nonce="{ request.custom_code_nonce }"')

    if custom_code:
        request.custom_code_output_content = True
        return str('\n' + custom_code)
    return ""

@receiver(process_response, dispatch_uid="custom_code_process_response")
def process_response_signal(sender, request, response, **kwargs):
    if not getattr(request, "custom_code_output_content", None):
        return response
    if "Content-Security-Policy" in response:
        headers = _parse_csp(response["Content-Security-Policy"])
    else:
        headers = {}

    _merge_csp(
        headers,
        {
            "script-src": [f"'nonce-{request.custom_code_nonce}'", sender.settings.get("plausible_url")],
            "style-src": [f"'nonce-{request.custom_code_nonce}'"],
        },
    )
    if headers:
        response["Content-Security-Policy"] = _render_csp(headers)

    return response

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