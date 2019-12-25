import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'#os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT = 465#int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False# os.environ.get('MAIL_USE_TLS') is not None
    MAIL_DEBUG = True
    MAIL_USERNAME = '112063126@qq.com'# os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'ujttontxucqpcagb'# os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = '112063126@qq.com'
    ADMINS = ['112063126@qq.com']
    POSTS_PER_PAGE = 3
