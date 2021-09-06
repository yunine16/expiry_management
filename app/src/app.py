from flask import Flask
from flask_restful import Api
from database import init_db
import models

app = Flask(__name__)
app.config.from_object('config.Config')

init_db(app)
api = Api(app)

if __name__ == "__main__" :
    app.run()