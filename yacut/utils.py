import random
from string import ascii_letters, digits

from .models import URLMap


def check_unique_short_id(short):
    return bool(URLMap.query.filter_by(short=short).first())


def get_unique_short_id():
    letters_and_digits = ascii_letters + digits
    rand_string = ''.join(random.sample(letters_and_digits, 6))
    if check_unique_short_id(rand_string):
        get_unique_short_id()
    return rand_string