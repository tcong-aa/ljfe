#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager, Shell
from app import app

manager = Manager(app)

def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
