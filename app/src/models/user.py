from datetime import datetime
from database import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mailAddress = db.Column(db.String(255), nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    foods = db.relationship('Food', backref='owner')

    def __init__(self, mailAddress=None):
        self.mailAddress = mailAddress

    def __str__(self):
        return "mailAddress = %s" % self.mailAddress