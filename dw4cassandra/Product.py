from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType
from cassandra.cqlengine import columns
from cassandra.cqlengine import management


class ProductUserType(UserType):
    nameLength = columns.Integer()
    descriptionLength = columns.Integer()
    photosTotal = columns.Integer()
    weightGrams = columns.Integer()
    lengthCm = columns.Integer()
    heightCm = columns.Integer()
    widthCm = columns.Integer()
    categoryNameEnglish = columns.Text()


class Product(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'product'
    __connection__ = 'cluster1'
    id = columns.VarInt(primary_key=True)
    categoryName = columns.Text(primary_key=True)
    data = columns.UserDefinedType(ProductUserType)


management.sync_table(Product)
