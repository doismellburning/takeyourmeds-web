"""
Django settings for nhs_reminder project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = "/accounts/login"

# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'reminder',
    'telephony',
    'djcelery',
    'rest_framework',
    'allauth',
    'allauth.account',
    'payments'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'nhs_reminder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'nhs_reminder.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://localhost:6379/0'


import django12factor
custom_settings = [
    'STRIPE_PUBLIC_KEY',
    'STRIPE_SECRET_KEY',
    'TW_ACCOUNT_SID',
    'TW_ACCOUNT_SID',
    'TW_AUTH_TOKEN',
]
d12f = django12factor.factorise()

ALLOWED_HOSTS = d12f['ALLOWED_HOSTS']
DATABASES = d12f['DATABASES']
DEBUG = d12f['DEBUG']
SECRET_KEY = d12f['SECRET_KEY']
STRIPE_PUBLIC_KEY = d12f.get('STRIPE_PUBLIC_KEY', 'pk_test_KVrAfaHNBkN15KR1Oi8pLWL6')
STRIPE_SECRET_KEY = d12f.get('STRIPE_SECRET_KEY', 'sk_test_cPNACljvxG4Uw8BnEH2Fi90N')
TW_ACCOUNT_SID = d12f.get('TW_ACCOUNT_SID', 'xxxxx')
TW_AUTH_TOKEN = d12f.get('TW_AUTH_TOKEN', 'xxxxx')
TW_FROM_NUMBER = d12f.get('TW_FROM_NUMBER', '+44....')
