from datetime import timedelta

from .environment import env


OBSOLETE_FEATURES = env.list("OBSOLETE_FEATURES", default=[])

OBSOLETE_EMAIL_FROM = env.str("OBSOLETE_EMAIL_FROM", default="no-reply@example.com")

OBSOLETE_AUTH_COOKIE_NAME = env.str("OBSOLETE_AUTH_COOKIE_NAME", default="a")

# Reset password link lifetime interval (in seconds). By default: 1 hour.
OBSOLETE_RESET_PASSWORD_EXPIRATION_DELTA = timedelta(seconds=env.int("OBSOLETE_RESET_PASSWORD_EXPIRATION_DELTA", default=3600))

if "LOG_SQL" in OBSOLETE_FEATURES:  # pragma: no cover
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
        "formatters": {
            "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
            "verbose": {"format": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"},
            "sql": {"()": "obsolete.loggers.SQLFormatter", "format": "[%(duration).3f] %(statement)s"},
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "verbose", "level": "DEBUG"},
            "sql": {"class": "logging.StreamHandler", "formatter": "sql", "level": "DEBUG"},
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["sql"],
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "propagate": False,
            },
            "django.db.backends.schema": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        },
    }
