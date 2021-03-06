#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager, Shell
from app import app

manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def generate_week_values():
    from week_data_converter.converter import save_to_db_month, save_to_db_week
    save_to_db_week()
    save_to_db_month()

@manager.command
def create_tables():
    from week_data_converter.converter import WeekPrice, MonthPrice
    # WeekPrice.__table__.create(app.db.session.bind)
    MonthPrice.__table__.create(app.db.session.bind)


if __name__ == '__main__':
    manager.run()
