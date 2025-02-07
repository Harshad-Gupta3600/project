class Config(object):
    DEBUG = False 
    TESTING = False 

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///mad2.db'
    SECRET_KEY = '47143bfe00aa76f30892f2f88a1676f27a0d2901c458f1c369271ae3fcd49f2e'
    SECURITY_PASSWORD_SALT='thisissalt'
    SQLAlCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'    