from application.settings import BASE_DIR

DATABASES = {  # remove for production
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DEBUG = True  # disable for production
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']  # enter list for production
