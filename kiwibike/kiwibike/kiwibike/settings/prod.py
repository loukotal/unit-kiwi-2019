import sys

from .base import *  # noqa

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': False,
}

ALLOWED_HOSTS += os.getenv("PROD_URL").split()  # noqa

CORS_ORIGIN_WHITELIST = os.getenv("CORS_URL").split()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',  # change debug level as appropiate
            'propagate': True,
        },
    },
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
        'rest_framework.renderers.JSONRenderer',
        )MEDIA_ROOT = '/media'
MEDIA_URL = '/files/'

# Sends emails to console


EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
