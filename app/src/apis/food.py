# Foodsテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from database import db
from models import User, Food

# 全ての食品に関するクラス
# /foods
class FoodList(Resource):
    def get(self):
        return

    def post(self):
        return

# ある食品に関するクラス
# /foods/<id>
class Food(Resource):
    def get(self):
        return

    def put(self):
        return

    def delete(self):
        return

# あるuserの所有する食品一覧に関するクラス
# /foods/user/<user_id>
class UsersFoodList(Resource):
    def get(self):
        return