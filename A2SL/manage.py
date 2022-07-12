#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
    sys.path.append(str(ROOT_DIR / "A2SL"))
    #print( os.getcwd())
   # os.environ['DJANGO_SETTINGS_MODULE'] = 'A2SL.settings'
   #print(os.environ['DJANGO_SETTINGS_MODULE'])
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','A2SL.settings' )
   #print(os.environ['DJANGO_SETTINGS_MODULE'])
   
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #import django
    #django.setup()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
