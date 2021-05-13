from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class Product(Model):
    id = columns.Text(primary_key=True)
    category_name = columns.Text()
    nameLenght = columns.Integer()
    descriptionLenght = columns.Integer()
    photosTotal = columns.Integer()
    weightGrams = columns.Integer()
    lengthCm = columns.Integer()
    heightCm = columns.Integer()
    widthCm = columns.Integer()
