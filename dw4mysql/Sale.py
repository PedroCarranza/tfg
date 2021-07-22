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
    price = FloatField()
    freight_value = FloatField()
    hours_to_approval = IntegerField()
    hours_at_seller = IntegerField()
    hours_at_carrier = IntegerField()
    shipping_limit_date = DateTimeField()
    customer_id = ForeignKeyField(Customer)
    seller_id = ForeignKeyField(Seller)
    review_id = ForeignKeyField(Review)
    order_id = ForeignKeyField(OrderSales)
    product_id = ForeignKeyField(Product)
    payment_id = ForeignKeyField(Payment)


