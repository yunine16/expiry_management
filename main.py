from flask import Flask, jsonify
from db.database import init_db
from db.models import Food

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"

if __name__ == "__main__" :
    init_db()
    app.run(host="0.0.0.0", debug=True,threaded=True)
