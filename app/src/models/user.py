from datetime import datetime
from sqlalchemy_utils import UUIDType
from database import db
import uuid

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    # ここと
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # ここにかいてね