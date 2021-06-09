from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Seller(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'seller'
    __connection__ = 'cluster1'
    id = columns.BigInt(primary_key=True)
    zip_code_prefix = columns.Integer()
    city = columns.Text()
    state = columns.Text()


sync_table(Seller)
