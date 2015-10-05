import sys, os, django

home = os.path.expanduser("~")
sys.path.append(os.path.join(home, 'path/to/projectroot'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.active")
django.setup()
