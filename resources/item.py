from flask_restful import Resource
from flask import request

from models.item import ItemModel
from schemas.item import ItemSchema

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

class Item(Resource):
    @classmethod
    def get(cls, name: str):
        item = ItemModel.find_by_name(name)
        if item:
            return item_schema.dump(item), 200
        return {"message": "Item not found"}, 404

    @classmethod
    def post(cls, name: str):
        item_json = request.get_json()
        
        #if ItemModel.find_by_name(item_json['name']):
           # return {"message": "Item with this name already exist"}, 400
        
        
        item = item_schema.load(item_json)

        try:
            print(item)
            item.save_to_db()
        except:
            return {"message": "Error inserting in DB"}, 500
        
        return item_schema.dump(Item), 201

class ItemList(Resource):
    @classmethod
    def get(cls):
        return {"items" : item_list_schema.dump(ItemModel.find_all())}, 200
    
   

    