import re

from settings import ERROR_LENGTH, ERROR_VALUE, NO_ID, NO_URL, NOT_FOUND

from .error_handlers import InvalidAPIUsageError
from .models import URLMap


def valid_404(url_short):
    url = URLMap.query.filter_by(short=url_short).first()
    if not url:
        raise InvalidAPIUsageError(NO_ID, 404)
    return url.original


def valid_data(data):
    if not data:
        raise InvalidAPIUsageError(NOT_FOUND)
    if 'url' not in data:
        raise InvalidAPIUsageError(NO_URL)
    return False


def valid_short_id(short_id):
    if not re.search(r'^[a-zA-Z0-9]*\Z', short_id) or len(short_id) > 16:
        raise InvalidAPIUsageError(ERROR_VALUE)
    if URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsageError(ERROR_LENGTH)
    return False
