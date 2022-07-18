from pathlib import Path

from .environment import env


BASE_DIR = Path(__file__).resolve().parent.parent


def rel(*path):
    return BASE_DIR.joinpath(*path)


DEBUG = env.bool("OBSOLETE_DEBUG", default=False)

INTERNAL_IPS = env.list("OBSOLETE_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("OBSOLETE_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("OBSOLETE_SECRET_KEY")

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "rest_framework",
    "django_extensions",
    "django_filters",
    "drf_yasg",
    # our apps
    "obsolete.apps.common",
    "obsolete.apps.accounts",
] + env.list("OBSOLETE_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("OBSOLETE_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "obsolete.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "obsolete.wsgi.application"

DATABASES = {"default": env.db("OBSOLETE_DATABASE_URL", default="psql://postgres:root@database:5432/obsolete_db")}

AUTH_USER_MODEL = "accounts.UserAccount"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SECURE_BROWSER_XSS_FILTER = env.bool("OBSOLETE_SECURE_BROWSER_XSS_FILTER", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("OBSOLETE_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SESSION_COOKIE_HTTPONLY = env.bool("OBSOLETE_SESSION_COOKIE_HTTPONLY", default=True)
SESSION_COOKIE_SECURE = env.bool("OBSOLETE_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("OBSOLETE_CSRF_COOKIE_SECURE", default=True)
X_FRAME_OPTIONS = env.str("OBSOLETE_X_FRAME_OPTIONS", default="SAMEORIGIN")
SECURE_HSTS_SECONDS = env.int("OBSOLETE_SECURE_HSTS_SECONDS", default=31536000)  # 1 year
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_NAME = "c"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [rel("..", "..", "api", "locale")]

STATIC_URL = env.str("OBSOLETE_STATIC_URL", default="/s/")
STATIC_ROOT = env.str("OBSOLETE_STATIC_ROOT", default=rel("..", "..", "public", "static"))

MEDIA_URL = env.str("OBSOLETE_MEDIA_URL", default="/m/")
MEDIA_ROOT = env.str("OBSOLETE_MEDIA_ROOT", rel("..", "..", "public", "media"))

EMAIL_BACKEND = env.str("OBSOLETE_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":  # pragma: no cover
    EMAIL_HOST = env.str("OBSOLETE_EMAIL_HOST")
    EMAIL_PORT = env.str("OBSOLETE_EMAIL_PORT")
    EMAIL_HOST_USER = env.str("OBSOLETE_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env.str("OBSOLETE_EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env.bool("OBSOLETE_EMAIL_USE_TLS", default=True)

SITE_ID = env.int("OBSOLETE_SITE_ID", default=1)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
