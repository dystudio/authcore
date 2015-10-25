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
import datetime
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
    'rest_framework.authtoken',
    'rest_framework_expiring_authtoken',
    'authcore',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Only for browsable API.
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
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
    'authcore.middleware.StdExceptionMiddleware',
)

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

AUTH_USER_MODEL = 'authcore.User'


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


############################
# Extension configuration. #
############################
### Expiring auth tokens config. ###
EXPIRING_TOKEN_LIFESPAN = datetime.timedelta(days=1)


### JWT config. ###
# Commented items hold the default value.
JWT_AUTH = {
    # 'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    # 'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    # 'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    # 'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'authcore.serializers.jwt_response_payload_handler',
    # 'JWT_SECRET_KEY': SECRET_KEY,
    # 'JWT_ALGORITHM': 'HS256',
    # 'JWT_VERIFY': True,
    # 'JWT_VERIFY_EXPIRATION': True,
    # 'JWT_LEEWAY': 0,
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=15),
    # 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 'JWT_AUDIENCE': None,
    # 'JWT_ISSUER': None,
    # 'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
