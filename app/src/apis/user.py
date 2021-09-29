# Usersテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from database import db
from datetime import datetime
from models import User, food

parser = reqparse.RequestParser()
parser.add_argument('mailAddress')

# 全てのuserに関するクラス
# /users
class UserApi(Resource):
    def get(self):
        return

    def post(self):
        args = parser.parse_args()
        new_usr = User(args['mailAddress'])
        db.session.add(new_usr)
        db.session.commit()
        return

    def delete(self):
        return