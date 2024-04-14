"""
Django settings for test_back_end project.

Generated by 'django-admin startproject' using Django 4.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#4in3$s)4%5%c-&3+ca50#qos==_xh!=tue#pu-o*qo4sqn7&l'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

log_file_info = os.path.join("test_back_end/log/log_info.log")
log_file_error = os.path.join("test_back_end/log/log_error.log")

CORS_ORIGIN_ALLOW_ALL= True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
        'corsheaders',

    'produit'
]

MIDDLEWARE = [
   'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_back_end.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_back_end.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #La configuration d'accés à la BDD de monn localhost
    'default': {
        'ENGINE': 'mssql',
        'HOST': 'localhost\SQLEXPRESS',
        'USER':'root',
        'NAME':'test',
        'PASSWORD': 'sagem',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'isolation_level': 'READ UNCOMMITTED',
            "init_command": "SET foreign_key_checks = 0;",
        }

    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
#La configuration de log d'application
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
      'file_error': {
        'level': 'ERROR',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'formatter': 'standard',
        'filename':log_file_error,
        'when': 'D',  # Weekly rotation
        'backupCount': 0,  # No backup files
    },
      
     'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': log_file_info,
            'when': 'D',  # Weekly rotation
            'backupCount': 0,  # No backup files
        },
         
       
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'propagate': True,
            'handlers': ['file'],
        },
          'error_logger': { 
            'level': 'ERROR',
            'handlers': ['file_error'],
            'propagate': False,
        },
     },
    
    'root': {
        'level': 'ERROR',
        'handlers': ['file_error'],
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'