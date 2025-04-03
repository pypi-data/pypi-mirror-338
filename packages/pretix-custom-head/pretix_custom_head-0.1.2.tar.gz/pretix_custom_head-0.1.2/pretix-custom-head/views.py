from django import forms
from django.shortcuts import render, redirect
from pretix.control.permissions import event_permission_required

class HeadTrackingSettingsForm(forms.Form):
    custom_head_code = forms.CharField(widget=forms.Textarea, required=False)
    plausible_url = forms.URLField(required=False)
    plausible_domain = forms.CharField(required=False)

@event_permission_required("can_change_event_settings")
def head_tracking_settings(request, event):
    if request.method == "POST":
        form = HeadTrackingSettingsForm(request.POST)
        if form.is_valid():
            event.settings.custom_head_code = form.cleaned_data["custom_head_code"]
            event.settings.plausible_url = form.cleaned_data["plausible_url"]
            event.settings.plausible_domain = form.cleaned_data["plausible_domain"]
            event.settings.save()
            return redirect("plugins:head_tracking_settings", event.slug)
    else:
        form = HeadTrackingSettingsForm(initial={
            "custom_head_code": event.settings.custom_head_code,
            "plausible_url": event.settings.plausible_url,
            "plausible_domain": event.settings.plausible_domain,
        })

    return render(request, "pretix_custom_head/settings.html", {"form": form, "event": event})