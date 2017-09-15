from flask import Flask, jsonify, make_response

from flask import render_template, request

from extensions import db

from week_data_converter.converter import WeekPrice, MonthPrice, CommunityMeta, HouseMeta

import logging
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    # app.config.from_object(settings)
    app.config.from_object('config')

    db.init_app(app)
    app.db = db

    register_blueprints(app)
    # register_extensions(app)
    # register_errorhandlers(app)
    # register_listeners(app)

    return app


def register_blueprints(app):
    @app.route('/')
    def index():
        return render_template('index.html', title='Hommy Candle Stick')

    @app.route('/community')
    def community():
        code = request.args.get('code')
        community = db.session.query(CommunityMeta).filter(CommunityMeta.id==code).first()

        return jsonify({
            "code": community.id,
            "name": community.name,
            "district_name": community.district_name,
            "bizcircle_name": community.bizcircle_name,
            "address": community.address,
            "favorite_count": community.favorite_count,
            "build_year": community.build_year,
            "build_type": community.build_type
        })


    @app.route('/month_prices')
    def month_prices():

        code = request.args.get('code')

        month_prices = db.session.query(MonthPrice).filter(MonthPrice.community_code==code).all()

        prices_rows = []

        for month_price in month_prices:
            prices_rows.append({
                "open": month_price.open,
                "close": month_price.close,
                "high": month_price.high,
                "low": month_price.low,
                "volumn": month_price.volumn
            })

        return jsonify({
            "code": code,
            "prices": prices_rows
        })

    @app.route('/week_prices')
    def week_prices():

        code = request.args.get('code')

        week_prices = db.session.query(WeekPrice).filter(WeekPrice.community_code==code).all()

        prices_rows = []

        for week_price in week_prices:
            prices_rows.append({
                "open": week_price.open,
                "close": week_price.close,
                "high": week_price.high,
                "low": week_price.low,
                "volumn": week_price.volumn
            })

        return jsonify({
            "code": code,
            "prices": prices_rows
        })

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

app = create_app()
