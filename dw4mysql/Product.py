from peewee import *
from dw4mysql.BaseModel import BaseModel


class Product(BaseModel):
    id = UUIDField(primary_key=True)
    category_name = CharField()
    name_length = IntegerField(null=True)
    description_length = IntegerField(null=True)
    photos_total = IntegerField(null=True)
    weight_grams = IntegerField(null=True)
    length_cm = IntegerField(null=True)
    height_cm = IntegerField(null=True)
    width_cm = IntegerField(null=True)
    category_name_english = CharField(null=True)

    class Meta:
        db_table = 'product'


Product.create_table()


