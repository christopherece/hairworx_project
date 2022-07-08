# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p&r%&k5v2a(q91iqtbjvi9wgoi70mug$=!&0syo$xs*zprqk^@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.10.232','hairworx.ddns.net','119.224.29.234']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hairworx',
        'USER': 'hairworx',
        'PASSWORD': '@dm!nL0c@lH0$t',
    }
}
