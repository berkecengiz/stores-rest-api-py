from flask import Flask
from flask_restful import Api
from flask_jwt import JWT                                           # Jason Web Token

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from datetime import timedelta
from db import db

app = Flask(__name__)
app.secret_key = 'secretkey12345'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'         # SQLalchemy configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # turn of flask sqlalchemy track modifications
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)        # 30 minutes expiration time

jwt = JWT(app, authenticate, identity)                              # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')          # http://127.0.0.1/item/chair
api.add_resource(ItemList, '/items')                   # http://127.0.0.1/items
api.add_resource(UserRegister, '/register')            # http://127.0.0.1/register


if __name__ == '__main__':
    app.run(port=5000, debug=True)
