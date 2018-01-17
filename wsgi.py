#! -*- coding:utf8 -*-

import os
import sys
from django.core.wsgi import get_wsgi_application

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(base_path)

sys.stdout = sys.stderr
os.system('export PYTHONIOENCODING=utf-8')

SETTINGS = 'web.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS)

application = get_wsgi_application()