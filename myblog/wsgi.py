"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
PROJECT_DIR=dirname(dirname(abspath(__file__)))
import sys

sys.path.insert(0,PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE']='myblog.settings'

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

application = get_wsgi_application()
