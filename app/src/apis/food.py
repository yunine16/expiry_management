# Foodsテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from flask import jsonify, abort
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

    def delete(self):
        return

# あるuserの所有する食品一覧に関するクラス
# /foods/user/<user_id>


class UsersFoodListApi(Resource):
    def get(self, user_id):
        foods = db.session.query(Food).filter_by(user_id=user_id).all()
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            abort(404, {'code': 'Not found', 'message': 'user not found'})
        return jsonify({
            "UsersFoodList": [
                {"id": food.id,
                 "name": food.name,
                 "expiry_date": food.expiry_date,
                 "user_id": food.user_id
                 } for food in foods]
        })
