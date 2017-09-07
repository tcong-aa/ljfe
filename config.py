import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_user = 'deliver'
db_pass = 'deliver'
db_host = 'db'
db_port = 5432
db_name = 'deliver'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    db_user, db_pass, db_host, db_port, db_name
)

DEBUG=True
