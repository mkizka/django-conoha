from django.conf import settings


def load_settings(k, default=None):
    return getattr(settings, k, default)
