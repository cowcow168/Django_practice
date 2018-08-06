"""
Django settings for mySite project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rs(js&^3ozd9%^lw1jwc&n8!frjk(1bhorq3762v7i^@hzj&kp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'books.apps.BooksConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #herokuでgunicornの説明があるので追記
    'gunicorn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mySite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #現在のパスを取得する(manage.pyと同じ階層にするtemplatesフォルダーにパスを通す)
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
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

WSGI_APPLICATION = 'mySite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'DJANGO', #データベース名
        'USER': 'ushijima', #ユーザーID
        'PASSWORD': 's05g2008A', #ユーザーIDのパスワード
        'HOST': '127.0.0.1', #ホスト名,別のホストを指定する場合は「xxx.xxx.xxx.xxx」のようにIPアドレスを指定できる。
        # 'PORT': '3306',
    }
}

#herokuとデバッグ環境を切り分ける COMPUTER-NAMEは、デバイス名
#
# if "COMPUTER-NAME" in hostname:
#     #デバッグ環境
#     DATABASES = {
#         'default': {
#             # 'ENGINE': 'django.db.backends.sqlite3',
#             'ENGINE': 'django.db.backends.mysql',
#             # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#             'NAME': 'DJANGO',  # データベース名
#             'USER': 'ushijima',  # ユーザーID
#             'PASSWORD': 's05g2008A',  # ユーザーIDのパスワード
#             'HOST': '127.0.0.1',  # ホスト名,別のホストを指定する場合は「xxx.xxx.xxx.xxx」のようにIPアドレスを指定できる。
#             # 'PORT': '3306',
#         }
#     }
#     ALLOWED_HOSTS = []
# else:
#     #本番環境
#     import dj_database_url
#     db_from_env = dj_database_url.config()
#     DATABASES = {
#         # 'default': dj_database_url.config()
#         'default': db_from_env
#     }
#     ALLOWED_HOSTS = ['*']




# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

#上の設定がデフォルト
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
