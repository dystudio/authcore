"""Django settings for the authcore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

For REST framework settings, see
http://www.django-rest-framework.org/api-guide/settings/

For database registry and configuration, see
https://docs.djangoproject.com/en/1.8/ref/settings/#databases

For i18n and l10n, see
https://docs.djangoproject.com/en/1.8/topics/i18n/

For static resources, see
https://docs.djangoproject.com/en/1.8/howto/static-files/

For JWT settings, see
http://getblimp.github.io/django-rest-framework-jwt/

For Guardian settings, see
http://django-guardian.readthedocs.org/en/v1.2/configuration.html

TODO(TheDodd): Quick-start development settings - unsuitable for production,
see https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
"""
import datetime
import os

# Ensure needed env variables are in place for development.
if not os.getenv('AUTHCORE_BACKEND_HOST'):
    raise RuntimeError('AUTHCORE_BACKEND_HOST must be specified for development.')

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
    'guardian',
    'authcore',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
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
    'authcore_project.middleware.StdExceptionMiddleware',
)

ROOT_URLCONF = 'authcore_project.urls'

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

WSGI_APPLICATION = 'authcore_project.wsgi.application'


###################
# REST framework. #
###################
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authcore_project.authentication.JSONWebTokenAuthenticationWithNonce',
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


##############
# Databases. #
##############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'authcore',
        'PASSWORD': 'authcoreadmin',
        'HOST': os.environ['AUTHCORE_BACKEND_HOST'],
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


#######################
# Extension settings. #
#######################
### JWT settings. ###
# Commented items hold the default value.
JWT_AUTH = {
    # 'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    # 'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER': 'authcore.serializers.jwt_payload_handler',
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


### Guardian settings. ###
ANONYMOUS_USER_ID = None
GUARDIAN_RAISE_403 = True
