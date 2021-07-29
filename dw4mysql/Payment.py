from peewee import *
from dw4mysql.BaseModel import BaseModel


class Payment(BaseModel):
    id = UUIDField(primary_key=True)
    payment_type = CharField(null=False)
    payment_installments = IntegerField(null=False)
    payment_value = FloatField(null=False)

    class Meta:
        db_table = 'payment'


Payment.create_table()


