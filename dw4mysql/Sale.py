from peewee import *
from dw4mysql.BaseModel import BaseModel
from dw4mysql.Customer import Customer
from dw4mysql.Seller import Seller
from dw4mysql.Review import Review
from dw4mysql.OrderSales import OrderSales
from dw4mysql.Product import Product
from dw4mysql.Payment import Payment


class Sale(BaseModel):
    id = UUIDField(primary_key=True)
    price = FloatField(null=False)
    freight_value = FloatField(null=False)
    hours_to_approval = IntegerField(null=True)
    hours_at_seller = IntegerField(null=True)
    hours_at_carrier = IntegerField(null=True)
    shipping_limit_date = DateTimeField(null=False)
    customer_id = ForeignKeyField(Customer, to_field='unique_id', backref='sales', null=True)
    seller_id = ForeignKeyField(Seller, to_field='id', backref='sales', null=True)
    review_id = ForeignKeyField(Review, to_field='id', backref='sales', null=True)
    order_id = ForeignKeyField(OrderSales, to_field='id', backref='sales', null=True)
    product_id = ForeignKeyField(Product, to_field='id', backref='sales', null=True)
    payment_id = ForeignKeyField(Payment, to_field='id', backref='sales', null=True)

    class Meta:
        db_table = 'sale'


Sale.create_table()


