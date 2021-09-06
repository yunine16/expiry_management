import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/expiry_management?charset=UTF8'.format(
        **{
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_ROOT_PASSWORD', 'em_root_pass'),
            'host': os.getenv('DB_HOST', 'db')
    })

    print(os.getenv('DB_ROOT_PASSWORD'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig