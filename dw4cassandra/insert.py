import csv
import os
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

connection.register_connection('cluster1', ['127.0.0.1'])

from dw4cassandra.Product import Product

with open('../csv/olist_products_dataset.csv') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    readerProd.next()
    for row in readerProd:
        product = Product(id=long(row[0]),
                       categoryName=row[1],
                       nameLength=(int(row[2]) if row[2] != '' else None),
                       descriptionLength=(int(row[3]) if row[3] != '' else None),
                       photosTotal=(int(row[4]) if row[4] != '' else None),
                       weightGrams=(int(row[5]) if row[5] != '' else None),
                       lengthCm=(int(row[6]) if row[6] != '' else None),
                       heightCm=(int(row[7]) if row[7] != '' else None),
                       widthCm=(int(row[8]) if row[8] != '' else None))
        product.save()
