from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ... (typical Django settings)
DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

SECRET_KEY = os.environ.get('SECRET_KEY')
