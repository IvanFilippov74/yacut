from . import app
from .models import URLMap


@app.route('/')
def index_view():
    pass