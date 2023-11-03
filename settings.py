import os

ERROR_LENGTH = 'Предложенный вариант короткой ссылки уже существует.'
ERROR_VALUE = 'Указано недопустимое имя для короткой ссылки'
NO_ID = 'Указанный id не найден'
NO_URL = '"url" является обязательным полем!'
NOT_FOUND = 'Отсутствует тело запроса'


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
