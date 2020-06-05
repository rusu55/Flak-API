from flask import Flask
from flask_restful import Api

from db import db
from ma import ma

from resources.user import UserRegister, User
from resources.item import ItemList, Item


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")

api.add_resource(Item, "/item/<string:name>")

api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)