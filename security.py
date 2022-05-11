# Authentication and logging
# Introducting the db to our program

import hmac
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):      # safe string compression, safer way to compare strings
        print(UserModel)
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
