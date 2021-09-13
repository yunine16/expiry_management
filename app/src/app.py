from flask import Flask
from flask_restful import Api
from database import init_db
from apis.user import UserApi
from apis.food import FoodListApi, FoodApi, UsersFoodListApi

app = Flask(__name__)
app.config.from_object('config.Config')

init_db(app)
api = Api(app)

api.add_resource(UserApi, "/users")
api.add_resource(FoodListApi, "/foods")
api.add_resource(FoodApi, "/foods/<id>")
api.add_resource(UsersFoodListApi, "/foods/user/<int:user_id>")

if __name__ == "__main__" :
    app.run()