# Usersテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from database import db
from models import User, food

# 全てのuserに関するクラス
# /users
class UserApi(Resource):
    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return