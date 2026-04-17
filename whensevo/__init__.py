import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DATABASE'] = os.path.join(app.instance_path, 'events.db')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import timegrab
    app.register_blueprint(timegrab.bp)

    return app
