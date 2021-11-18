from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Customer(Model):
    __keyspace__ = 'dw4cassandra'
    __table_name__ = 'customer'
    __connection__ = 'cluster1'
    type_name = 'customer'
    id = columns.UUID(primary_key=True)
    zip_code_prefix = columns.Integer()
    city = columns.Text()
    state = columns.Text()


sync_table(Customer)
