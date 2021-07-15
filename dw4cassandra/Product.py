from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine import management


class Product(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'product'
    __connection__ = 'cluster1'
    id = columns.VarInt(primary_key=True)
    category_name = columns.Text(primary_key=True)
    name_length = columns.Integer()
    description_length = columns.Integer()
    photos_total = columns.Integer()
    weight_grams = columns.Integer()
    length_cm = columns.Integer()
    height_cm = columns.Integer()
    width_cm = columns.Integer()
    category_name_english = columns.Text()


management.sync_table(Product)
