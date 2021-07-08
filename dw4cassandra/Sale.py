from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Sale(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'sale'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)
    price = columns.Float()
    freightValue = columns.Float()
    hoursToApproval = columns.Integer()
    hoursAtSeller = columns.Integer()
    hoursAtCarrier = columns.Integer()
    shippingLimitDate = columns.DateTime()
    customerId = columns.VarInt()
    sellerId = columns.VarInt()
    reviewId = columns.VarInt()
    orderId = columns.VarInt()
    productId = columns.VarInt()
    paymentId = columns.VarInt()


sync_table(Sale)
