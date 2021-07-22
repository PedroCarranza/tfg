from peewee import *
from dw4mysql.BaseModel import BaseModel


class OrderSales(BaseModel):
    id = UUIDField(primary_key=True)
    status = CharField()
    purchase = DateTimeField()
    approved_at = DateTimeField()
    delivered_carrier = DateTimeField()
    delivered_customer = DateTimeField()
    estimated_delivery = DateField()


