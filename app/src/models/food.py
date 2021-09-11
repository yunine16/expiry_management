
from datetime import datetime
from database import db

class Food(db.Model):
    __tablename__ = 'Foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, name=None, expiry_date=None, user_id=None):
        self.name = name
        self.expiry_date = expiry_date
        self.user_id = user_id

    def __str__(self):
        return "name = %s, expiry_date = %s, user_id = %d" % (self.name, self.expiry_date, self.user_id)
