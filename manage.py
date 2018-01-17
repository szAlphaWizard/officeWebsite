#! -*- coding:utf -*-
import os
import sys
from django.core.management import execute_from_command_line

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.insert(0, base_path)

CONFIG_MODULE = "web.settings"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", CONFIG_MODULE)
    execute_from_command_line(sys.argv)
