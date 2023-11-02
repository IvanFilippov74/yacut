from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLMapForm(FlaskForm):
    original = URLField(
        'Введите ваш длинный URL',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256, message='Длинна поля от 4 до 256 символов'),
            URL(message='Введите коректный URL адрес, http://ваша_ссылка'),
        ]
    )
    short = StringField(
        'Введите ваш вариант',
        validators=[
            Length(1, 16, message='Длинна поля от 6 до 16 символов'),
            Optional(),
            Regexp(
                '[A-z0-9]',
                message='Для ссылки допустимы символы латинского '
                        'алфавита и цифры от 0 до 9'
            )
        ]
    )
    submit = SubmitField('Создать')