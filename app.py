from flask import Flask, jsonify, make_response
from flask import render_template, request
from extensions import db
from week_data_converter.converter import WeekPrice, MonthPrice, CommunityMeta, HouseMeta
from sqlalchemy import desc
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__,
                static_url_path='',
                static_folder='static',
                template_folder='templates')
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
        limit_num = request.args.get('limit')
        if not limit_num:
            limit_num = 10

        community = db.session.query(CommunityMeta).filter(CommunityMeta.id == code).first()

        if code == '100000':

            deals = db.session.query(HouseMeta).order_by(
                desc(HouseMeta.deal_time)).limit(limit_num)

        else:

            deals = db.session.query(HouseMeta).filter(HouseMeta.community_id == code).order_by(
                desc(HouseMeta.deal_time)).limit(limit_num)

        recent_deals = []
        for deal in deals:
            recent_deals.append({
                "deal_time": deal.deal_time,
                "unit_price": deal.unit_price,
                "community_name": deal.community_name,
                "area": deal.area,
                "price": deal.price
            })

        return jsonify({
            "code": community.id,
            "name": community.name,
            "district_name": community.district_name,
            "bizcircle_name": community.bizcircle_name,
            "address": community.address,
            "favorite_count": community.favorite_count,
            "build_year": community.build_year,
            "build_type": community.build_type,
            "recent_deals": recent_deals
        })

    @app.route('/proxy')
    def proxy():

        import requests, json

        r = requests.get('http://52.23.237.85:8080/search?text=%E7%82%AB%E7%89%B9')

        r1 = {
            "rows": [{
                "address": "shifoying xuantejiayuan",
                "bizcircle_name": "shiw=foying",
                "build_type": "",
                "build_year": "2005-2007",
                "code": "1111027381238",
                "district_name": "chaoyang",
                "favorite_count": "2518",
                "name": "xuantejiayuan"
            }]
        }

        return json.dumps(r.json())

    @app.route('/search')
    def search():
        input_text = request.args.get('text')
        communities = db.session.query(CommunityMeta).filter(CommunityMeta.name.like("%{}%".format(input_text))).all()
        rows = []

        for community in communities:
            rows.append({
                "code": community.id,
                "name": community.name,
                "district_name": community.district_name,
                "bizcircle_name": community.bizcircle_name,
                "address": community.address,
                "favorite_count": community.favorite_count,
                "build_year": community.build_year,
                "build_type": community.build_type
            })

        return jsonify({
            "rows": rows
        })

    @app.route('/month_prices')
    def month_prices():

        code = request.args.get('code')

        month_prices = db.session.query(MonthPrice).filter(MonthPrice.community_code == code).all()

        prices_rows = []

        for month_price in month_prices:
            prices_rows.append({
                "date": month_price.date.strftime('%Y-%m-%d'),
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

        week_prices = db.session.query(WeekPrice).filter(WeekPrice.community_code == code).all()

        prices_rows = []

        for week_price in week_prices:
            prices_rows.append({
                "date": week_price.date.strftime('%Y-%m-%d'),
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
