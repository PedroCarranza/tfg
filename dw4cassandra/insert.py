import csv
from dw4cassandra.Product import Product
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

with open('../csv/olist_products_dataset.csv') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    #cluster = Cluster()
    #session = cluster.connect()

    connection.register_connection('cluster1', ['127.0.0.1'])

    readerProd.next()
    for row in readerProd:
        product = Product(id=(row[0]),
                       categoryName=row[1],
                       nameLength=int(row[2]),
                       descriptionLength=int(row[3]),
                       photosTotal=int(row[4]),
                       weightGrams=int(row[5]),
                       lengthCm=int(row[6]),
                       heightCm=int(row[7]),
                       widthCm=int(row[8]))
        product.save()
        print(row[0])
