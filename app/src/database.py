from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)