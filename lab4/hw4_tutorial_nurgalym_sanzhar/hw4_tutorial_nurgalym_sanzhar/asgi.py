"""
ASGI config for hw4_tutorial_nurgalym_sanzhar project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw4_tutorial_nurgalym_sanzhar.settings')

application = get_asgi_application()
