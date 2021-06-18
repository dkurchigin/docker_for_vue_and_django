"""
WSGI config for simple_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/simple_api')
sys.path.append('/var/www/simple_api/simple_api')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_api.settings')

application = get_wsgi_application()
