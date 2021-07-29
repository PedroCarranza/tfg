from peewee import *
from dw4mysql.BaseModel import BaseModel


class OrderSales(BaseModel):
    id = UUIDField(primary_key=True)
    status = CharField(null=False)
    purchase = DateTimeField(null=False)
    approved_at = DateTimeField(null=False)
    delivered_carrier = DateTimeField(null=False)
    delivered_customer = DateTimeField(null=False)
    estimated_delivery = DateField(null=False)

    class Meta:
        db_table = 'order_sales'


OrderSales.create_table()


