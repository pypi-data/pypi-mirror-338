from django.apps import AppConfig

class CustomHeadTrackingConfig(AppConfig):
    name = "pretix_custom_head"
    verbose_name = "Custom Head Injection & Tracking"
    def ready(self):
        from . import signals  # noqa