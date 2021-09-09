
from datetime import datetime
from sqlalchemy_utils import UUIDType
from database import db
import uuid

class Food(db.Model):
    __tablename__ = 'Foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    expiry_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)