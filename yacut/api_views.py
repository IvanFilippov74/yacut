from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .models import URLMap
from .utils import get_unique_short_id
from .validators import valid_404, valid_data, valid_short_id


@app.route('/api/id/<string:url_short>/', methods=['GET'])
def get_opinion(url_short):
    return jsonify({'url': valid_404(url_short)}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_opinion():
    data = request.get_json()
    valid_data(data)
    url = URLMap()
    custom_id = data.get('custom_id', None)
    if not custom_id or custom_id is None:
        custom_id = get_unique_short_id()
        data.update({'custom_id': custom_id})
    valid_short_id(custom_id)
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
