from .base import * 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#現在路徑的前前一個資料夾
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0+(4&&n6ex0pb3*q$nyp=e2d3-q&f7y+$sqndh7ql1s$=+1!e0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True