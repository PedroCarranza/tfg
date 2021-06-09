import csv
import os
from cassandra.cqlengine import connection

if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

connection.register_connection('cluster1', ['127.0.0.1'])

from dw4cassandra.Product import Product
from dw4cassandra.Customer import Customer
from dw4cassandra.Seller import Seller
from dw4cassandra.Review import Review

with open('../csv/olist_products_dataset.csv') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    readerProd.next()

    for row in readerProd:
        product = Product(id=int(row[0], 16),
                          categoryName=row[1],
                          nameLength=(int(row[2]) if row[2] != '' else None),
                          descriptionLength=(int(row[3]) if row[3] != '' else None),
                          photosTotal=(int(row[4]) if row[4] != '' else None),
                          weightGrams=(int(row[5]) if row[5] != '' else None),
                          lengthCm=(int(row[6]) if row[6] != '' else None),
                          heightCm=(int(row[7]) if row[7] != '' else None),
                          widthCm=(int(row[8]) if row[8] != '' else None))
        product.save()

with open('../csv/olist_customers_dataset.csv') as csvCus:
    readerCus = csv.reader(csvCus, delimiter=',', quotechar='"')

    readerCus.next()

    for row in readerCus:
        customer = Customer(uniqueId=int(row[1], 16),
                            zip_code_prefix=(int(row[2]) if row[2] != '' else None),
                            city=row[3],
                            state=row[4])
        customer.save()

with open('../csv/olist_sellers_dataset.csv') as csvSel:
    readerSel = csv.reader(csvSel, delimiter=',', quotechar='"')

    readerSel.next()

    for row in readerSel:
        seller = Seller(id=int(row[0], 16),
                        zip_code_prefix=(int(row[2]) if row[1] != '' else None),
                        city=row[2],
                        state=row[3])
        seller.save()

with open('../csv/olist_order_reviews_dataset.csv') as csvRev:
    readerRev = csv.reader(csvRev, delimiter=',', quotechar='"')

    readerRev.next()

    for row in readerRev:
        review = Review(id=int(row[0], 16),
                        score=(int(row[2]) if row[1] != '' else None),
                        comment_title=row[2],
                        creation_date=row[3],
                        answer_timestamp=row[4])
        review.save()
