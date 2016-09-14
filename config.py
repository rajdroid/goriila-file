import os


basedir = os.path.abspath(os.path.dirname(__file__))


"""
    Base Configuration class. Configurations present in this class
    are inherited by all specific environment (development, production,
    staging) configuration classess
"""
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', default='hard to guess')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


"""
    Development specific configurations are specified in this class.
"""
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI',
        default='sqlite:////' + os.path.join(basedir, 'data-dev.sqlite'))
    UPLOAD_FOLDER = 'uploads'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}