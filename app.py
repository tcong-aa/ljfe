from flask import Flask, jsonify, make_response

import logging
logger = logging.getLogger(__name__)

def create_app():

    app = Flask(__name__)
    # app.config.from_object(settings)
    app.config.from_object('config')

    # db.init_app(app)
    # app.db = db

    register_blueprints(app)
    # register_extensions(app)
    # register_errorhandlers(app)
    # register_listeners(app)

    return app


def register_blueprints(app):
    @app.route('/')
    def index():
        return jsonify({'successed': True})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

app = create_app()
