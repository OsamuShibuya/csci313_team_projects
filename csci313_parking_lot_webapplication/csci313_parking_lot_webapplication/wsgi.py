"""
WSGI config for csci313_parking_lot_webapplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "csci313_parking_lot_webapplication.settings"
)

application = get_wsgi_application()
