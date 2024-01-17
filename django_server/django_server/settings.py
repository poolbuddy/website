from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-oz6f*l823wejg_afj55s%_k+1cg9foy1)knde$%!8v@@$pv^3*'

SECURE_SSL_REDIRECT = False

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
SITE_ID = 1 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',

    'django.contrib.sites',  # Required for django-meta
    'meta',
    'robots_txt',
    'django_seo_js',
    

    'accounts',
    'apps.blog',
    'apps.store',
    'apps.forms',
    'apps.customer_profile'
]

AUTH_USER_MODEL = 'accounts.User'
SEO_JS_PRERENDER_TOKEN = "123456789abcdefghijkl"
MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_seo_js.middleware.HashBangMiddleware', 
    'django_seo_js.middleware.UserAgentMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')
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

WSGI_APPLICATION = 'django_server.wsgi.application'


DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'my_django_db'),
        'USER': os.environ.get('POSTGRES_USER', 'steve'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '123'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),  # Use the service name from Docker Compose  # Set to the appropriate host if your database is on a different server
        'PORT': '5432',       # Set to the appropriate port
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media' ) # Absolute filesystem path to the directory that will hold media.
MEDIA_URL = "/media/"            # URL that handles the media served from MEDIA_ROOT.

STATIC_URL = 'static/'
STATIC_ROOT = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated'
    ),
} 

# Use the console email backend for testing

# The following settings are not needed for console backend but can be kept
# if you plan to switch back to an SMTP backend for actual email sending

# SMTP server settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SMTP server settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Your Gmail account credentials
EMAIL_HOST_USER = 'info@thepoolbuddy.com'
EMAIL_HOST_PASSWORD = 'donkeysSMELL420!'

DJOSER = {
    "USER_ID_FIELD":"email",
    "LOGIN_FIELD":"email",
    'PASSWORD_RESET_CONFIRM_URL': '#/auth/password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SERIALIZERS': {
            'user_create': 'accounts.serializers.CustomUserCreateSerializer'
    }
}