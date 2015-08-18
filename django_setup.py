import sys, os, django

home = os.path.expanduser("~")
sys.path.append(os.path.join(home, 'leetcode/noj'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.active")
django.setup()
