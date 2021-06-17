from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Customer(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'costumer'
    __connection__ = 'cluster1'
    type_name = 'costumer'
    uniqueId = columns.VarInt(primary_key=True)
    zip_code_prefix = columns.Integer()
    city = columns.Text()
    state = columns.Text()


sync_table(Customer)
