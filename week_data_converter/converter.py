from datetime import datetime, timedelta
from extensions import db
from sqlalchemy import desc
from itertools import groupby


class WeekPrice(db.Model):
    __tablename__ = 'hommy_week_price'

    date = db.Column(db.Date, primary_key=True)

    community_code = db.Column(db.Text, index=True)
    name = db.Column(db.Text, index=True)

    open = db.Column(db.Float)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)

class HouseMeta(db.Model):

    __tablename__ = 'house_meta'

    house_code = db.Column(db.Text, primary_key=True)

    community_name = db.Column(db.Text)
    community_id = db.Column(db.Text)
    area = db.Column(db.Text)
    unit_price = db.Column(db.Text)
    price = db.Column(db.Text)
    deal_time = db.Column(db.Text)


def get_sunday(curr_date):
    curr_date = datetime.strptime(curr_date, '%Y.%m.%d')
    start = curr_date - timedelta(days=(curr_date.weekday() + 1) % 7)
    return start + timedelta(days=7)


def construct_sunday_values():
    house_meta_coll = db.session.query(HouseMeta).filter(HouseMeta.deal_time!="").order_by(desc(HouseMeta.deal_time)).all()
    total_deals = dict()

    for community_id, house_meta in groupby(house_meta_coll, key=lambda meta: meta['community_id']):

        total_deals.setdefault(community_id, {
            'community_id': community_id,
            'community_name': house_meta.community_name
        })


        #
        # for house_meta in house_meta_coll:
        #     if house_meta.deal_time:
        #
        #         sunday = get_sunday(house_meta.deal_time)
        #         date_str = sunday.strftime('%Y-%m-%d')
        #
        #         total_deals.setdefault()
        #
        #         total_deals.setdefault(date_str, [])
        #
        #         total_deals[date_str].append(house_meta)

    return total_deals


def save_to_db():

    total_values = construct_sunday_values()

    print total_values

    # for sunday, deals in total_values.items():
    #     print sunday, deals
    #
    #     # prices = map(lambda deal: deal.)
    #
    #     WeekPrice(
    #         date=sunday,
    #
    #     )


