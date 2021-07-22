from peewee import *
from dw4mysql.BaseModel import BaseModel


class Seller(BaseModel):
    id = UUIDField(primary_key=True)
    zip_code_prefix = IntegerField()
    city = CharField()
    state = CharField()
