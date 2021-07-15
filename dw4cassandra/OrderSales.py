from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class OrderSales(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'ordersales'
    __connection__ = 'cluster1'
    id = columns.VarInt(primary_key=True)
    status = columns.Text()
    purchase = columns.DateTime()
    approved_at = columns.DateTime()
    delivered_carrier = columns.DateTime()
    delivered_customer = columns.DateTime()
    estimated_delivery = columns.Date()


sync_table(OrderSales)
