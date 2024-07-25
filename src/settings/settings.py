from split_settings.tools import include

from settings.compontents.base_dir import BASE_DIR as BASE_DIR_C
from settings.envs import get_settings

settings = get_settings()

include("compontents/*.py")

BASE_DIR = BASE_DIR_C

SECRET_KEY = settings.app.secret_key

DEBUG = settings.app.debug

ALLOWED_HOSTS = settings.app.allowed_hosts

ROOT_URLCONF = "settings.urls"

WSGI_APPLICATION = "settings.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
