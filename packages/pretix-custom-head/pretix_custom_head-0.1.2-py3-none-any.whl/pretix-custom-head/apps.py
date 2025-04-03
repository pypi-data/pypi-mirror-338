from django.utils.translation import gettext_lazy as _
from pretix.base.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "pretix_custom_head"
    verbose_name = _("Custom Head Injection & Plausible Tracking")

    class PretixPluginMeta:
        name = _("Custom Head Injection & Plausible Tracking")
        author = "Bergruebe"
        description = _("Fügt beliebigen Code in den <head> ein und trackt Bestellungen mit Plausible Analytics.")
        visible = True
        version = "0.1.2"
        compatibility = "pretix>=4.0.0"

    def ready(self):
        from . import signals  # noqa