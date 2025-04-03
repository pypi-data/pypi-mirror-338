from django.urls import path
from .views import head_tracking_settings

urlpatterns = [
    path("settings/", head_tracking_settings, name="head_tracking_settings"),
]