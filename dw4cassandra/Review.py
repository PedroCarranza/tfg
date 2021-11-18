from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table


class Review(Model):
    __keyspace__ = 'dw4cassandra'
    __table_name__ = 'review'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)
    review_id = columns.UUID()
    score = columns.Integer()
    comment_title = columns.Text()
    comment_message = columns.Text()
    creation_date = columns.Text()
    answer_timestamp = columns.Text()


sync_table(Review)
