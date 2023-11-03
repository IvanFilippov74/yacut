from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите ваш длинный URL',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256, message='Длинна поля от 1 до 256 символов'),
            URL(message='Введите коректный URL адрес, http:// + ваша_ссылка'),
        ]
    )
    custom_id = StringField(
        'Введите ваш вариант',
        validators=[
            Length(1, 16, message='Длинна поля от 1 до 16 символов'),
            Optional(),
            Regexp(
                '[A-z0-9]',
                message='Для ссылки допустимы символы латинского '
                        'алфавита и цифры от 0 до 9.'
            )
        ]
    )
    submit = SubmitField('Создать')