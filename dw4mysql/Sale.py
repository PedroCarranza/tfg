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
    hours_to_approval = IntegerField(null=False)
    hours_at_seller = IntegerField(null=False)
    hours_at_carrier = IntegerField(null=False)
    shipping_limit_date = DateTimeField(null=False)
    customer_id = ForeignKeyField(Customer, to_field='unique_id', backref='sales', null=False)
    seller_id = ForeignKeyField(Seller, to_field='id', backref='sales', null=False)
    review_id = ForeignKeyField(Review, to_field='id', backref='sales', null=False)
    order_id = ForeignKeyField(OrderSales, to_field='id', backref='sales', null=False)
    product_id = ForeignKeyField(Product, to_field='id', backref='sales', null=False)
    payment_id = ForeignKeyField(Payment, to_field='id', backref='sales', null=False)

    class Meta:
        db_table = 'sale'


Sale.create_table()


