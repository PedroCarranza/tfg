from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Sale(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'sale'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)
    price = columns.Float()
    freight_value = columns.Float()
    hours_to_approval = columns.Integer()
    hours_at_seller = columns.Integer()
    hours_at_carrier = columns.Integer()
    shipping_limit_date = columns.DateTime()
    customer_id = columns.VarInt()
    seller_id = columns.VarInt()
    review_id = columns.VarInt()
    order_id = columns.VarInt()
    product_id = columns.VarInt()
    payment_id = columns.UUID()


sync_table(Sale)
