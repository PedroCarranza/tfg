from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Payment(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'payment'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)


sync_table(Payment)
