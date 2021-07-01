from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType
from cassandra.cqlengine import columns
from cassandra.cqlengine import management


class ProductUserType(UserType):
    __type_name__ = 'productUserType'
    id = columns.VarInt(primary_key=True)
    categoryname = columns.Text(primary_key=True)
    namelength = columns.Integer()
    descriptionlength = columns.Integer()
    photostotal = columns.Integer()
    weightgrams = columns.Integer()
    lengthcm = columns.Integer()
    heightcm = columns.Integer()
    widthcm = columns.Integer()
    categorynameenglish = columns.Text()


class Product(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'product'
    __connection__ = 'cluster1'
    productId = columns.UUID(primary_key=True)
    data = columns.UserDefinedType(ProductUserType)


management.sync_table(Product)
