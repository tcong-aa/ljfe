from datetime import datetime, timedelta
from extensions import db
from sqlalchemy import desc, UniqueConstraint
from itertools import groupby
import calendar


class MonthPrice(db.Model):
    __tablename__ = 'hommy_month_price'

    __table_args__ = (
        UniqueConstraint("date", "community_code"),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    date = db.Column(db.Date, index=True)
    community_code = db.Column(db.Text, index=True)
    name = db.Column(db.Text, index=True)

    open = db.Column(db.Float)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    volumn = db.Column(db.BigInteger)


class WeekPrice(db.Model):
    __tablename__ = 'hommy_week_price'

    __table_args__ = (
        UniqueConstraint("date", "community_code"),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    date = db.Column(db.Date, index=True)
    community_code = db.Column(db.Text, index=True)
    name = db.Column(db.Text, index=True)

    open = db.Column(db.Float)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    volumn = db.Column(db.BigInteger)

    def __repr__(self):
        return "date: {}, community: {}, open: {}, close: {}, high: {}, low: {}, volumn: {}".format(
            self.date,
            self.community_code,
            self.open,
            self.close,
            self.high,
            self.low,
            self.volumn
        )

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

def get_month_end_day(curr_date):
    curr_date = datetime.strptime(curr_date, '%Y.%m.%d')
    day = calendar.monthrange(curr_date.year, curr_date.month)

    date = "{}-{}-{}".format(curr_date.year, curr_date.month, day)
    return date


def construct_sunday_values():
    house_meta_coll = db.session.query(HouseMeta).filter(HouseMeta.deal_time!="").order_by(desc(HouseMeta.deal_time)).all()
    total_deals = dict()

    for community_id, house_metas in groupby(house_meta_coll, lambda meta:meta.community_id):
        for house_meta in house_metas:

            total_deals.setdefault(community_id, {
                'community_id': community_id,
                'community_name': house_meta.community_name,
                'deals': {}
            })

            sunday = get_sunday(house_meta.deal_time)
            date_str = sunday.strftime('%Y-%m-%d')

            total_deals[community_id]['deals'].setdefault(date_str, [])
            total_deals[community_id]['deals'][date_str].append(house_meta)

    return total_deals


def save_to_db_week():

    total_values = construct_sunday_values()

    for community_id, community_info in total_values.items():
        name = community_info['community_name']

        for date, house_metas in community_info['deals'].items():

            prices = map(lambda house_meta: float(house_meta.unit_price), house_metas)
            price = WeekPrice(
                date=date,
                name=name,
                community_code=community_id,
                open=prices[0],
                close=prices[-1],
                high=max(prices),
                low=min(prices),
                volumn=len(prices)
            )

            print price

            db.session.add(price)

    db.session.commit()

def save_to_db_month():

    house_meta_coll = db.session.query(HouseMeta).filter(HouseMeta.deal_time!="").order_by(desc(HouseMeta.deal_time)).all()
    total_deals = dict()

    for community_id, house_metas in groupby(house_meta_coll, lambda meta:meta.community_id):
        for house_meta in house_metas:

            total_deals.setdefault(community_id, {
                'community_id': community_id,
                'community_name': house_meta.community_name,
                'deals': {}
            })

            month_end = get_month_end_day(house_meta.deal_time)
            # date_str = month_end.strftime('%Y-%m-%d')

            total_deals[community_id]['deals'].setdefault(month_end, [])
            total_deals[community_id]['deals'][month_end].append(house_meta)


    for community_id, community_info in total_deals.items():
        name = community_info['community_name']

        for date, house_metas in community_info['deals'].items():

            prices = map(lambda house_meta: float(house_meta.unit_price), house_metas)
            price = MonthPrice(
                date=date,
                name=name,
                community_code=community_id,
                open=prices[0],
                close=prices[-1],
                high=max(prices),
                low=min(prices),
                volumn=len(prices)
            )

            print price

            # db.session.add(price)

    # db.session.commit()

