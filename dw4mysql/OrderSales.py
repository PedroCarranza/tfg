from peewee import *
from dw4mysql.BaseModel import BaseModel


class OrderSales(BaseModel):
    id = UUIDField(primary_key=True)
    status = CharField(null=True)
    purchase = DateTimeField(null=True)
    approved_at = DateTimeField(null=True)
    delivered_carrier = DateTimeField(null=True)
    delivered_customer = DateTimeField(null=True)
    estimated_delivery = DateField(null=True)

    class Meta:
        db_table = 'order_sales'


OrderSales.create_table()


