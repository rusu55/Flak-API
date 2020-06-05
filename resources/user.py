from flask_restful import Resource
from flask import request

from models.user import UserModel
from schemas.user import UserSchema

user_schema = UserSchema()

class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if(UserModel.find_by_username(user.username)):
            return {"message": "User already exist!"}, 400
        
        user.save_to_db()   
        
        return {"message": "User succesfully created!"}, 201

class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message" : "User not found"}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404
        user.delete_from_db()
        return {"message" : "User deleted!"}, 
        
   
   