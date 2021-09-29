from datetime import datetime
from flask_restful import Resource, reqparse, abort
from database import db
from models import User, Food
class FoodCheckApi(Resource):
    def get(self,user_id):
        day=datetime.date.today()+datetime.timedelta(days=7)
        expired_food=db.session.query(Food).filter(Food.user_id==user_id,Food.expirly_date<=day).all()
        return expired_food