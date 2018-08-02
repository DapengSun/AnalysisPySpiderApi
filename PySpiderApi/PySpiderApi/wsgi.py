"""
WSGI config for PySpiderApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys
sys.path.append("/var/www/AnalysisPySpiderApi/PySpiderApi/PySpiderApi")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PySpiderApi.settings")

application = get_wsgi_application()
