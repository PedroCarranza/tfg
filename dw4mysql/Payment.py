from peewee import *
from dw4mysql.BaseModel import BaseModel


class Payment(Model):
    id = UUIDField(primary_key=True)
    payment_type = CharField()
    payment_installments = IntegerField()
    payment_value = FloatField()


