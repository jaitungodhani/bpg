#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bpg_project.settings')
    # os.environ.setdefault('BPG_ENVIRONMENT', 'DEV')
    # os.environ.setdefault('DJANGO_DEBUG', '1')
    # os.environ.setdefault('DJANGO_SECRET_KEY', 'abcd1234')
    # os.environ.setdefault('DJANGO_STATIC_URL', '/static/')
    # os.environ.setdefault('DJANGO_STATIC_ROOT', 'static')
    # os.environ.setdefault('WEBSITE_HOSTNAME', '127.0.0.1')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
