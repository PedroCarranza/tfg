import csv
from dw4cassandra.Product import Product
from cassandra.cluster import Cluster

with open('../csv/olist_products_dataset.csv', newline='') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    cluster = Cluster()
    session = cluster.connect("dw4cassandra")

    for row in readerProd:
        Product.create(id=row[0], nameLength=int(row[1]),
                       descriptionLenght=int(row[2]),
                       photosTotal=int(row[3]),
                       weightGrams=int(row[4]),
                       lengthCm=int(row[5]),
                       heightCm=int(row[6]),
                       widthCm=int(row[7]))
