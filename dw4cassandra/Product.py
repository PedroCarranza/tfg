from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table

class Product(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'product'
    __connection__ = 'cluster1'
    id = columns.BigInt(primary_key=True)
    categoryName = columns.Text()
    nameLength = columns.Integer()
    descriptionLength = columns.Integer()
    photosTotal = columns.Integer()
    weightGrams = columns.Integer()
    lengthCm = columns.Integer()
    heightCm = columns.Integer()
    widthCm = columns.Integer()

sync_table(Product)