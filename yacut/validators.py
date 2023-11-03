import re

from settings import NO_ID, NOT_FOUND, NO_URL, ERROR_LENGTH, ERROR_VALUE
from .error_handlers import InvalidAPIUsage
from .models import URLMap

def valid_404(url_short):
    url = URLMap.query.filter_by(short=url_short).first()
    if not url:
        raise InvalidAPIUsage(NO_ID, 404)
    return url.original

def valid_data(data):
    if not data:
        raise InvalidAPIUsage(NOT_FOUND)
    if 'url' not in data:
        raise InvalidAPIUsage(NO_URL)
    return None

def valid_short_id(short_id):
    if not re.search(r'^[a-zA-Z0-9]*\Z', short_id) or len(short_id) > 16:
        raise InvalidAPIUsage(ERROR_VALUE)
    if URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsage(ERROR_LENGTH)
    return None
