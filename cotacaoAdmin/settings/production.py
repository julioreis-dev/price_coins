from cotacaoAdmin.settings.settings import *

DEBUG = True

SECRET_KEY = 'django-insecure-r05@$*8=pv@gg0yht@+lhbn8ifiqotd1_u29mb-f3kez(f@moe'

# Alterar para o IP do ambiente de produção quando houver.
ALLOWED_HOSTS = ['challengebr.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}
