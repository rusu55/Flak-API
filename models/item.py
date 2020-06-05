from typing import List
from db import db


class ItemModel(db.Model):
    __tablename__="items"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable = False, unique= True)
    price = db.Column(db.Float(precision=2), nullable = False)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("StoreModel")

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls, name: str) -> "ItemModel":
        result = cls.query.filter_by(name=name).first()
        
        return result

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        

