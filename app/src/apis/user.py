# Usersテーブルに関するスクリプトはここ
from flask_restful import Resource, reqparse, abort
from database import db
from models import User, food

# 全てのuserに関するクラス
# /users
class UserApi(Resource):
    def get(self):
        return

    def post(self, user_name, mailAddress, ):
        import time
        date=datetime.date.today()
        user_a=Users(name=user_name, mailAddress=mailAddress, created_at=date, updated_at=date, )
        db.session.add(user_a)
        db.session.flush()
        return

    def delete(self):
        return