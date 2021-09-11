from flask import Flask
from flask_restful import Api
from database import init_db
import models
from apis.user import User
from apis.food import FoodList, Food, UsersFoodList

app = Flask(__name__)
app.config.from_object('config.Config')

init_db(app)
api = Api(app)

api.add_resource(User, "/users")
api.add_resource(FoodList, "/foods")
api.add_resource(Food, "/foods/<id>")
api.add_resource(UsersFoodList, "/foods/user/<user_id>")

if __name__ == "__main__" :
    app.run()