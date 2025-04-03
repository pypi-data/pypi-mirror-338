"""Wrapper replacing Django's default "manage.py" file."""

import os
import sys


def manage():
    """Run administrative tasks (replaces 'manage.py')."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diop_core.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
