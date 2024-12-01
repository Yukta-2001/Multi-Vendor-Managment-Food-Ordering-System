"""
Django settings for foodline_main project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
temp_dir=os.path.join(BASE_DIR,'template')
static_dir=os.path.join(BASE_DIR,'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "vendor",
    "menu",
    "marketplace",
    "customer",
    "orders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #custom middleware created to access the request object in models.py
    "orders.request_object.RequestObjectMiddleware",
]

ROOT_URLCONF = "foodline_main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [temp_dir],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "accounts.context_processor.get_vendor",
                "marketplace.context_processor.get_cart_counter",
                "marketplace.context_processor.get_cart_amount",
                "accounts.context_processor.get_user_profile",
                #"accounts.context_processor.get_google_api",
                "accounts.context_processor.get_paypal_client_id",

                
            ],
        },
    },
]

WSGI_APPLICATION = "foodline_main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME'),
        "USER":config('DB_USER'),
        "PASSWORD":config('DB_PASSWORD'),
        "HOST":config('DB_HOST'),
    }
}
AUTH_USER_MODEL='accounts.User'

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_DIRS=[static_dir]
#media configuration
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
from django.contrib.messages import constants as messages
MESSAGE_TAGS={
    messages.ERROR:'danger',
}
#EMAIL CONFIGURATION
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='tayadearyan98@gmail.com'
EMAIL_HOST_PASSWORD='lisu vcru fwsa soaz'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='Foodonline Marketplace <tayadearyan98@gmail.com>'

#GOOGLE_API_KEY="AIzaSyD8xOstoZNWl9wfZ-eWF-7mGx5EzdKLseY" 
PAYPAL_CLIENT_ID='AWN7YlTx3A4S6vO8E7MmV6nw-c45wIuu-iXW7RZeJZvfRoSb6gMvxXc3maHjszdrNQwdoobJ0e4F9PLp'
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
#PAYPAL_SECRETE_KEY='EPtJs9g428uX0nfUThCnxriZ4ZAIXWCeUXFsSWjom4iMxz8imPRGH4_00FIEp0FsMbqHhrZwXn--i0I_'