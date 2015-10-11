"""Django settings for this project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

For database registry and configuration, see
https://docs.djangoproject.com/en/1.8/ref/settings/#databases

For i18n and l10n, see
https://docs.djangoproject.com/en/1.8/topics/i18n/

For static resources, see
https://docs.djangoproject.com/en/1.8/howto/static-files/

TODO(TheDodd): Quick-start development settings - unsuitable for production,
see https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
"""
import os

# Additional paths in this project should be built as such: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e+7%s=(8c86s#-3t6%o58q&)&iv(89isjrfyv0mlr772bofxf-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
POST_MORTEM = True

ALLOWED_HOSTS = []


###########################
# Application definition. #
###########################
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'authcore',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 100,
}

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

ROOT_URLCONF = 'appcore.urls'

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

WSGI_APPLICATION = 'appcore.wsgi.application'


##############
# Databases. #
##############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'authcore',
        'USER': 'authcoreadmin',
        'PASSWORD': 'authcoreadmin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


#########################
# Internationalization. #
#########################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###########################################
# Static files (CSS, JavaScript, Images). #
###########################################
STATIC_URL = '/static/'
