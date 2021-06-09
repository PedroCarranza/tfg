from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Review(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'review'
    __connection__ = 'cluster1'
    id = columns.BigInt(primary_key=True)
    score = columns.Integer()
    comment_title = columns.Text()
    creation_date = columns.Text()
    answer_timestamp = columns.Date()


sync_table(Review)
