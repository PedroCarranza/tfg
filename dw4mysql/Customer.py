from peewee import *
from dw4mysql.BaseModel import BaseModel


class Customer(BaseModel):
    unique_id = UUIDField(primary_key=True)
    zip_code_prefix = IntegerField(null=False)
    city = CharField(null=False)
    state = CharField(null=False)

    class Meta:
        db_table = 'customer'


Customer.create_table()