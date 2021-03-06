import os
import platform


class Config:
    # Database config.
    MONGODB_SETTINGS = {
        'db': 'test',
        'host': '127.0.0.1',
        'port': 27017
    }

    # LOCAL_DATA_PATH used for storing the raw data from crawling the github.
    LOCAL_DATA_PATH = os.environ.get('INFOX_LOCAL_DATA_PATH')

    # Overview page config.
    SHOW_NUMBER_FOR_PAGE = 6 # Project number per page in index page.
    SHOW_NUMBER_FOR_FORKS = 15 # Forks number per page in project overview page.

    # User manage config.
    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')

    # secret key is a random string.
    SECRET_KEY = os.environ.get('INFOX_SECRET_KEY')

    # E-mail Config
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get('INFOX_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('INFOX_MAIL_PASSWORD')
    FLASK_MAIL_SENDER = '<375833274@qq.com>'
    FLASK_MAIL_SUBJECT_PREFIX = '[INFOX]'


class DevelopmentConfig(Config):
    DEBUG = True
    RECRAWLER_MODE = False # Refresh will re-crawler the forks' info.

class ProductionConfig(Config):
    RECRAWLER_MODE = False # Refresh will re-crawler the forks' info.

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
