"""
Python 3.8
Generated by 'django-admin startproject' using Django 3.0.8.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Путь к корню проекта

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gbkhkfhzjm4545gsrg564sfkl_j6456sf455ds46dkn*jkjk54'                                            # |Поменяй|

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True                                                                                             # /Переключи\
# DEBUG = False                                                                                            # \Переключи/

# ALLOWED_HOSTS = []                                                                                        # /Переключи\
ALLOWED_HOSTS = ['fasschool.ru']                                                                         # \Переключи/


# Application definition

INSTALLED_APPS = [  # Какие приложения активны в нашем проекте
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'homepage',
    'enrollment',
]

MIDDLEWARE = [  # Список подключённых промежуточных слоёв
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fas_website.urls'  # Модуль, который содержит корневые шаблоны url-ов приложения

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'fas_website.wsgi.application'


# Database

DATABASES = {  # Настройки для всех баз данных проекта
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

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


# Internationalization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'  # Какой URL у статиков
STATIC_DIR = os.path.join(BASE_DIR, 'static')  # Директория со статикой
STATICFILES_DIRS = [STATIC_DIR]  # Список, из каких директорий нужно собирать статику
# STATIC_ROOT = '/home/users/a/annaturaszowa/projects/FAS/FAS_website/static/'                 #|Отключи при разработке|


MEDIA_URL = '/media/'  # URL для медии в шаблонах
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
