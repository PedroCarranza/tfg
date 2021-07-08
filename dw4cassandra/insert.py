import csv
import os
import uuid

from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from datetime import datetime

if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
    os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

connection.register_connection('cluster1', ['127.0.0.1'])

from dw4cassandra.Sale import Sale
from dw4cassandra.Product import Product
from dw4cassandra.Customer import Customer
from dw4cassandra.Seller import Seller
from dw4cassandra.Review import Review
from dw4cassandra.Order import Order

#   session = Cluster.connect(keyspace='olist')

with open('../csv/olist_products_dataset.csv') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    readerProd.next()

    cont = 0
    for row in readerProd:
        product = Product(productId=uuid.uuid4(),
                            id=int(row[0], 16),
                            categoryName=row[1],
                            nameLength=(int(row[2]) if row[2] != '' else None),
                            descriptionLength=(int(row[3]) if row[3] != '' else None),
                            photosTotal=(int(row[4]) if row[4] != '' else None),
                            weightGrams=(int(row[5]) if row[5] != '' else None),
                            lengthCm=(int(row[6]) if row[6] != '' else None),
                            heightCm=(int(row[7]) if row[7] != '' else None),
                            widthCm=(int(row[8]) if row[8] != '' else None),
                            categoryNameEnglish='')
        product.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de inserir no product")

with open('../csv/product_category_name_translation.csv') as csvTrans:
    readerTrans = csv.reader(csvTrans, delimiter=',', quotechar='"')

    readerTrans.next()

    for row in readerTrans:
        for product in Product.objects.filter(categoryName=row[0]).allow_filtering():
            product.categoryNameEnglish = row[1]
            product.update()

print("Acabei de alterar o product")

with open('../csv/olist_customers_dataset.csv') as csvCus:
    readerCus = csv.reader(csvCus, delimiter=',', quotechar='"')

    readerCus.next()

    cont = 0
    for row in readerCus:
        customer = Customer(uniqueId=int(row[1], 16),
                            zip_code_prefix=(int(row[2]) if row[2] != '' else None),
                            city=row[3],
                            state=row[4])
        customer.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de inserir no customer")

with open('../csv/olist_sellers_dataset.csv') as csvSel:
    readerSel = csv.reader(csvSel, delimiter=',', quotechar='"')

    readerSel.next()

    cont = 0
    for row in readerSel:
        seller = Seller(id=int(row[0], 16),
                        zip_code_prefix=(int(row[1]) if row[1] != '' else None),
                        city=row[2],
                        state=row[3])
        seller.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de inserir no seller")


with open('../csv/olist_order_reviews_dataset.csv') as csvRev:
    readerRev = csv.reader(csvRev, delimiter=',', quotechar='"')

    readerRev.next()

    cont = 0
    for row in readerRev:
        review = Review(id=int(row[0], 16),
                        score=(int(row[2]) if row[2] != '' else None),
                        comment_title=row[3],
                        comment_message=row[4],
                        creation_date=row[5],
                        answer_timestamp=row[6])
        review.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de inserir no review")

with open('../csv/olist_order_items_dataset.csv') as csvItens:
    readerItem = csv.reader(csvItens, delimiter=',', quotechar='"')

    readerItem.next()

    cont = 0
    for row in readerItem:
        sale = Sale(id=uuid.uuid4(),
                    price=float(row[5]) if row[5] != '' else None,
                    freightValue=float(row[6]) if row[6] != '' else None,
                    shippingLimitDate=datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S"),
                    orderId=int(row[0], 16),
                    sellerId=int(row[3], 16),
                    productId=int(row[2], 16))
        sale.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de inserir no sale")

with open('../csv/olist_orders_dataset.csv') as csvOrd:
    readerOder = csv.reader(csvOrd, delimiter=',', quotechar='"')

    readerOder.next()

    cont = 0
    for row in readerOder:
        purchase = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S") if row[3] != '' else None
        approvedAt = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S") if row[4] != '' else None
        deliveredCarrier = datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S") if row[5] != '' else None
        deliveredCustomer = datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S") if row[6] != '' else None
        estimatedDelivery = datetime.strptime(row[7], "%Y-%m-%d %H:%M:%S") if row[7] != '' else None

        for sales in Sale.objects.filter(orderId=int(row[0], 16)).allow_filtering():
            sales.customerId = int(row[1], 16)
            sales.hoursToApproval = int((approvedAt - purchase).total_seconds / 3600)
            sales.hoursAtSeller = int((deliveredCarrier - approvedAt).total_seconds / 3600)
            sales.hoursAtCarrier = int((deliveredCustomer - deliveredCarrier).total_seconds / 3600)
            sales.update()

        order = Order(id=int(row[0], 16),
                        status=row[2],
                        purchase=purchase,
                        approvedAt=approvedAt,
                        deliveredCarrier=deliveredCarrier,
                        deliveredCustomer=deliveredCustomer,
                        estimatedDelivery=estimatedDelivery)
        order.save()
        cont += 1
        if cont >= 100:
            break

print("Acabei de alterar o sale e inserir no Order")
