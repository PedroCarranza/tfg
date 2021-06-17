from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Order(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'order'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)


sync_table(Order)
