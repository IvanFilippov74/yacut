from flask import flash, redirect, render_template, url_for

from settings import ERROR_LENGTH
from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        url_short = form.custom_id.data
        if not url_short:
            url_short = get_unique_short_id()
        if URLMap.query.filter_by(short=url_short).first() is not None:
            flash(ERROR_LENGTH, 'error')
            return render_template('index.html', form=form)
        short_link = URLMap(
            original=form.original_link.data,
            short=url_short
        )
        db.session.add(short_link)
        db.session.commit()
        flash(url_for('get_short_url', url_short=url_short, _external=True), 'get_link')

    return render_template('index.html', form=form)


@app.route('/<string:url_short>')
def get_short_url(url_short):
    short_link = URLMap.query.filter_by(short=url_short).first_or_404()
    return redirect(short_link.original)
