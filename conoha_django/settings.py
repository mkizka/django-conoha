INSTALLED_APPS = [
    'conoha_django'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

SECRET_KEY = 'hogehogefugafuga'

USE_TZ = True
