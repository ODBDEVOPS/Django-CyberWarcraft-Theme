import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-fallback-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

INSTALLED_APPS = [
    'django_bootstrap5',
    'core.apps.CoreConfig',
]

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
    }
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
