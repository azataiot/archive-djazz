"""
         88  88
         88  ""
         88
 ,adPPYb,88  88  ,adPPYYba,  888888888  888888888
a8"    `Y88  88  ""     `Y8       a8P"       a8P"
8b       88  88  ,88djazz88    ,d8P'      ,d8P'
"8a,   ,d88  88  88,    ,88  ,d8"       ,d8"
 `"8bbdP"Y8  88  `"8bbdP"Y8  888888888  888888888
            ,88
          888P"

@azataiot - 2024 - Djazz! project
https://djazz.cc
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ****
# CORE
# ****

DEBUG = os.environ.get("DEBUG", "False")

# People who get code error notifications. In the format
# [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMINS = []

# List of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is True
#   * Receive x-headers
INTERNAL_IPS = []

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = []

# Local time zone for this installation. All choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = "UTC"

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LANGUAGE_CODE = "en-us"
LANGUAGES = [
    ("en", "English"),
]

# We don't use i18n here, as any internationalization should be done in the frontend.
USE_I18N = False

ROOT_URLCONF = 'djazz.urls'

# Whether to append trailing slashes to URLs.
APPEND_SLASH = True

WSGI_APPLICATION = 'djazz.wsgi.application'

# A secret key for this particular Django installation. Used in secret-key
# hashing algorithms. Set this in your settings, or Django will complain
# loudly.
SECRET_KEY = os.environ.get("SECRET_KEY", 'djazz-@ok-#c29$2024@(-a%3ozuk3ovlup97a+-1^*-5c_^x8u=a((&')

SITE_ID = 1

# ********
# DATABASE
# ********

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "postgres"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# *****
# EMAIL
# *****

# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Host for sending email.
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")

# Port for sending email.
EMAIL_PORT = os.environ.get("EMAIL_PORT", 1025)

# Email address that error messages come from.
SERVER_EMAIL = "root@localhost"
# Default email address to use for various automated correspondence from
# the site managers.

# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = "[Django] "

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "Djazz! <info@djazz.cc>")

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", False)
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL", False)
EMAIL_TIMEOUT = os.environ.get("EMAIL_TIMEOUT", None)

# ****
# APPS
# ****

INSTALLED_APPS = [
    # djazz accounts app (custom user model)
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# **********
# MIDDLEWARE
# **********

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# *********
# TEMPLATES
# *********

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ******
# STATIC
# ******

# Absolute path to the directory static files should be collected to.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = BASE_DIR / "data/static"

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled
# https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [BASE_DIR / "static"]

# *****
# MEDIA
# *****

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = BASE_DIR / "data/media"

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# *****
# CACHE
# *****

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ""
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = "default"

# **************
# AUTHENTICATION
# **************

AUTH_USER_MODEL = "accounts.User"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/accounts/profile/"
LOGOUT_REDIRECT_URL = None

# *******
# LOGGING
# *******

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# *****
# DEBUG
# *****
if DEBUG:
    # DEBUG ONLY SETTINGS
    import socket  # for docker development

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]

    # DEBUG ONLY APPS
    INSTALLED_APPS += [
        # Append django debug toolbar
        "debug_toolbar",
    ]

    # DEBUG ONLY MIDDLEWARE
    # Insert django debug toolbar middleware at the top
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
