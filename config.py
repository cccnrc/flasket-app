import os
from dotenv import load_dotenv

### this is to specify that I can also put these variables in a file called .env in main folder
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'DB', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['cocchi.e89@gmail.com']
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25) or 587
    MAIL_USE_TLS = bool( int( os.environ.get('MAIL_USE_TLS') or 1 ) )
    MAIL_USE_SSL = bool( int( os.environ.get('MAIL_USE_SSL') or 0 ) )
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'random-user'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'random-user-secret-password'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    TOKEN_EXP_SEC = os.environ.get('TOKEN_EXP_SEC') or 3600
    TOKEN_RESTORE_EXP_SEC = os.environ.get('TOKEN_RESTORE_EXP_SEC') or 3600
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') or 'aws-random-key'
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') or 'aws-random-secret-key'
    AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN') or 'aws-random-session-token'
    SES_REGION_NAME = os.environ.get('SES_REGION_NAME') or 'aws-random-region'
    SES_EMAIL_SOURCE = os.environ.get('SES_EMAIL_SOURCE') or 'SES'
    CREDENTIALS_URL = os.environ.get('CREDENTIALS_URL') or 'https://super-secret'
    SERVER_NAME = os.environ.get('SERVER_NAME') or '127.0.0.7:7000'
    LOCAL_DEVELOPMENT = os.environ.get('LOCAL_DEVELOPMENT') or 0
