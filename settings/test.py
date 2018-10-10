import os

from celery.app.task import Task


DEBUG = True

# Disable sending tasks in test mode.
Task.delay = lambda *args, **kwargs: None

SITE_URL = 'http://testserver'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT_TEST = os.path.join(BASE_DIR, 'media_test')
MEDIA_ROOT = MEDIA_ROOT_TEST
MEDIA_URL = '/media_test/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
