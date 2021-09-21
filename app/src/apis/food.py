# Foodsテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from database import db
from models import User, Food

# 全ての食品に関するクラス
# /foods
class FoodListApi(Resource):
    def get(self):
        return

    def post(self):
        return

# ある食品に関するクラス
# /foods/<id>
class FoodApi(Resource):
    def get(self):
        return

    def put(self):
        return

    def delete(self, mailAddress, name, expiry_date):
        id=db.session.query(Users).filter(Users.mailAddress==mailAddress)
        db.session.query(Foods).filter(Foods.name=name, Foods.user_id=id, Foods.expiry_date=expiry_date).delete()
        db.session.commit()
        return

# あるuserの所有する食品一覧に関するクラス
# /foods/user/<user_id>
class UsersFoodListApi(Resource):
    def get(self, user_id):
        user = db.session.query(Food).filter_by(user_id=user_id).all()
        return 