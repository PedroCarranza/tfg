from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine.management import sync_table
from dw4cassandra.Product import ProductUserType


class Sale(Model):
    __keyspace__ = 'olist'
    __table_name__ = 'sale'
    __connection__ = 'cluster1'
    id = columns.UUID(primary_key=True)
    price = columns.Float()
    freightValue = columns.Float()
    hoursToApproval = columns.Integer()
    hoursAtSeller = columns.Integer()
    hoursAtCarrier = columns.Integer()
    shippingLimitDate = columns.Date()
#   costumer = columns.UserDefinedType(Customer)
#   seller = columns.UserDefinedType(Seller)
#   review = columns.UserDefinedType(Review)
#   order = columns.UserDefinedType(Order)
    product = columns.UserDefinedType(ProductUserType)
#   payment = columns.UserDefinedType(Payment)


sync_table(Sale)
