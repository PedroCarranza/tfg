import csv
import uuid
from datetime import datetime
from Sale import Sale
from Product import Product
from Customer import Customer
from Seller import Seller
from Review import Review
from OrderSales import OrderSales
from Payment import Payment
from BaseModel import *
from peewee import *

create_tables()

with open('../csv/olist_products_dataset.csv') as csvProd:
    readerProd = csv.reader(csvProd, delimiter=',', quotechar='"')

    readerProd.next()

    for row in readerProd:
        product = Product(product_id=uuid.uuid4(),
                            id=int(row[0], 16),
                            category_name=row[1],
                            name_length=(int(row[2]) if row[2] != '' else None),
                            description_length=(int(row[3]) if row[3] != '' else None),
                            photos_total=(int(row[4]) if row[4] != '' else None),
                            weight_grams=(int(row[5]) if row[5] != '' else None),
                            length_cm=(int(row[6]) if row[6] != '' else None),
                            height_cm=(int(row[7]) if row[7] != '' else None),
                            width_cm=(int(row[8]) if row[8] != '' else None),
                            category_name_english='')
        product.save()

print("Acabei de inserir no product")

with open('../csv/product_category_name_translation.csv') as csvTrans:
    readerTrans = csv.reader(csvTrans, delimiter=',', quotechar='"')

    readerTrans.next()

    for row in readerTrans:
        for product in Product.objects.filter(category_name=row[0]).allow_filtering():
            product.categoryNameEnglish = row[1]
            product.update()

print("Acabei de alterar o product")

with open('../csv/olist_customers_dataset.csv') as csvCus:
    readerCus = csv.reader(csvCus, delimiter=',', quotechar='"')

    readerCus.next()

    for row in readerCus:
        customer = Customer(unique_id=int(row[1], 16),
                            zip_code_prefix=(int(row[2]) if row[2] != '' else None),
                            city=row[3],
                            state=row[4])
        customer.save()

print("Acabei de inserir no customer")

with open('../csv/olist_sellers_dataset.csv') as csvSel:
    readerSel = csv.reader(csvSel, delimiter=',', quotechar='"')

    readerSel.next()

    for row in readerSel:
        seller = Seller(id=int(row[0], 16),
                        zip_code_prefix=(int(row[1]) if row[1] != '' else None),
                        city=row[2],
                        state=row[3])
        seller.save()

print("Acabei de inserir no seller")

with open('../csv/olist_order_items_dataset.csv') as csvItens:
    readerItem = csv.reader(csvItens, delimiter=',', quotechar='"')

    readerItem.next()

    for row in readerItem:
        sale = Sale(id=uuid.uuid4(),
                    price=float(row[5]) if row[5] != '' else None,
                    freight_value=float(row[6]) if row[6] != '' else None,
                    shipping_limit_date=datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S"),
                    order_id=int(row[0], 16),
                    seller_id=int(row[3], 16),
                    product_id=int(row[2], 16))
        sale.save()

print("Acabei de inserir no sale")

with open('../csv/olist_orders_dataset.csv') as csvOrd:
    readerOder = csv.reader(csvOrd, delimiter=',', quotechar='"')

    readerOder.next()

    cont = 0
    for row in readerOder:
        purchase = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S") if row[3] != '' else None
        approved_at = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S") if row[4] != '' else None
        delivered_carrier = datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S") if row[5] != '' else None
        delivered_customer = datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S") if row[6] != '' else None
        estimated_delivery = datetime.strptime(row[7], "%Y-%m-%d %H:%M:%S") if row[7] != '' else None

        sales = Sale.objects.filter(order_id=int(row[0], 16)).allow_filtering()

        for sale in sales:
            sale.customer_id = int(row[1], 16)
            if (purchase is not None and approved_at is not None and delivered_carrier is not None and
                    delivered_customer is not None and estimated_delivery is not None):
                sale.hours_to_approval = int((approved_at - purchase).total_seconds() / 3600)
                sale.hours_at_seller = int((delivered_carrier - approved_at).total_seconds() / 3600)
                sale.hours_at_carrier = int((estimated_delivery - delivered_carrier).total_seconds() / 3600)
            else:
                sale.hours_to_approval = None
                sale.hours_at_seller = None
                sale.hours_at_carrier = None
            sale.update()

        #if len(sales) > 0:
        #    print("%d %d" % (len(sales), int(row[0], 16)))

        orderSales = OrderSales(id=int(row[0], 16),
                        status=row[2],
                        purchase=purchase,
                        approved_at=approved_at,
                        delivered_carrier=delivered_carrier,
                        delivered_customer=delivered_customer,
                        estimated_delivery=estimated_delivery)
        orderSales.save()
        cont += 1
        if cont % 1000 == 0:
            print('Contador: ', cont)

print("Acabei de inserir no OrderSale e alterar o Sale")

with open('../csv/olist_order_reviews_dataset.csv') as csvRev:
    readerRev = csv.reader(csvRev, delimiter=',', quotechar='"')

    readerRev.next()

    for row in readerRev:
        review = Review(id=int(row[0], 16),
                        score=(int(row[2]) if row[2] != '' else None),
                        comment_title=row[3],
                        comment_message=row[4],
                        creation_date=row[5],
                        answer_timestamp=row[6])
        review.save()

        sales = Sale.objects.filter(order_id=int(row[1], 16)).allow_filtering()

        for sale in sales:
            sale.review_id = review.id
            sale.update()

print("Acabei de inserir no review e alterar o Sale")

with open('../csv/olist_order_payments_dataset.csv') as csvPay:
    readerPay = csv.reader(csvPay, delimiter=',', quotechar='"')

    readerPay.next()

    for row in readerPay:
        payment = Payment(id=uuid.uuid4(),
                          payment_type=row[2],
                          payment_installments=(int(row[3]) if row[3] != '' else None),
                          payment_value=(float(row[4]) if row[4] != '' else None))
        payment.save()

        sales = Sale.objects.filter(order_id=int(row[0], 16)).allow_filtering()

        for sale in sales:
            sale.payment_id = payment.id
            sale.update()

        #if len(sales) > 0:
        #    print("%d %d" % (len(sales), int(row[0], 16)))

print("Acabei de inserir no payment e alterar o Sale")
