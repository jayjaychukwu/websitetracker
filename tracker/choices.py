from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class AuthorizationType(TextChoices):
    NONE = "NONE", _("None")
    BASICAUTH = "BASIC AUTH", _("Basic Auth")
    APIKEY = "API KEY", _("API Key")
    BEARERTOKEN = "BEARER TOKEN", _("Bearer Token")
    TOKEN = "TOKEN", _("Token")
