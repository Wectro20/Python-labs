from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import validate, fields, post_load
from marshmallow_enum import EnumField
from enum import Enum

db = SQLAlchemy()
ma = Marshmallow()


class Country(Enum):
    China = 0
    USA = 1
    Vietnam = 2


class Material(Enum):
    Cotton = 0
    Spandex = 1
    Polyester = 2


class Gender(Enum):
    Male = 0
    Female = 1
    Undefined = 2


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float())
    country = db.Column(db.Enum(Country))
    material = db.Column(db.Enum(Material))
    brand = db.Column(db.String(32))
    gender = db.Column(db.Enum(Gender))
    size = db.Column(db.String(32))
    type_of_sport = db.Column(db.String(32))
    name = db.Column(db.String(32))

    def __init__(self, name: str = " ", price: float = 0.0, country: Country = None, material: Material = None, brand: str = " ",
                 gender: Gender = None, size: str = " ", type_of_sport: str = " "):
        self.name = name
        self.price = price
        self.country = country
        self.material = material
        self.brand = brand
        self.gender = gender
        self.size = size
        self.type_of_sport = type_of_sport

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"Price: {self.price}\n " \
               f"Country: {self.country}\n " \
               f"Material: {self.material}\n " \
               f"Brand: {self.brand}\n" \
               f"Gender: {self.gender}\n " \
               f"Size: {self.size}\n " \
               f"Type of sport: {self.type_of_sport}\n "


class ItemSchema(ma.Schema):
    name = fields.Str(validate=validate.Length(min=0, max=32))
    price = fields.Float(validate=validate.Range(min=0.0, max=100000.0))
    country = EnumField(Country)
    material = EnumField(Material)
    brand = fields.Str(validate=validate.Length(min=0, max=32))
    gender = EnumField(Gender)
    size = fields.Str(validate=validate.Length(min=0, max=32))
    type_of_sport = fields.Str(validate=validate.Length(min=0, max=32))

    @post_load
    def make_item(self, data, **kwargs):
        return Item(**data)


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)




