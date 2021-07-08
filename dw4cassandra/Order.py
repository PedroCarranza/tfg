from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Order(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'order'
    __connection__ = 'cluster1'
    id = columns.VarInt(primary_key=True)
    status = columns.Text()
    purchase = columns.DateTime()
    approvedAt = columns.DateTime()
    deliveredCarrier = columns.DateTime()
    deliveredCustomer = columns.DateTime()
    estimatedDelivery = columns.Date()


sync_table(Order)
