from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Payment(Model):
    __keyspace__ = 'dw4cassandra'
    __table_name__ = 'payment'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)
    payment_type = columns.Text()
    payment_installments = columns.Integer()
    payment_value = columns.Float()


sync_table(Payment)
