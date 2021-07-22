from peewee import *
from dw4mysql.BaseModel import BaseModel


class Product(BaseModel):
    id = UUIDField(primary_key=True)
    category_name = CharField(primary_key=True)
    name_length = IntegerField()
    description_length = IntegerField()
    photos_total = IntegerField()
    weight_grams = IntegerField()
    length_cm = IntegerField()
    height_cm = IntegerField()
    width_cm = IntegerField()
    category_name_english = CharField


