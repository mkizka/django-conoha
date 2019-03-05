INSTALLED_APPS = [
    'conoha'
]

CONOHA_ACCESS_FILE_PATH = 'conoha.json'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

SECRET_KEY = 'hogehogefugafuga'

USE_TZ = True
