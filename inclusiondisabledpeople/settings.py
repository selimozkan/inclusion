from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "DjangoSecretKey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DJANGO_DEBUG") == "False" else True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",
    "ckeditor_uploader",
    "web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "inclusiondisabledpeople.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "inclusiondisabledpeople.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "inclusion.db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DATE_FORMAT = "d.m.Y"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static_files/"
STATICFILES_DIRS = [BASE_DIR / "static/"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"
if not DEBUG:
    MEDIA_ROOT = BASE_DIR / "media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        "height": 200,
        "width": "100%",
        "toolbar": "Custom",
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        "toolbar_Custom": [
            ["Format", "Font", "FontSize", "-", "TextColor", "BGColor"],
            [
                "Bold",
                "Italic",
                "Underline",
                "Strike",
                "Subscript",
                "Superscript",
                "RemoveFormat",
            ],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord", "Undo", "Redo"],
            ["Link", "Unlink", "-", "Image", "SpecialChar"],
            ["Maximize", "Source"],
        ],
    },
    "ckBasic": {
        "toolbar": "Basic",
    },
    "ckSimple": {
        "skin": "moono-lisa",
        "height": 150,
        "width": "100%",
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
    },
}

CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_PATH = ""

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "mail.inclusiondisabledpeople.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = False
EMAIL_HOST_USER = "web@inclusiondisabledpeople.com"
EMAIL_HOST_PASSWORD = "Parola.GT2024"
