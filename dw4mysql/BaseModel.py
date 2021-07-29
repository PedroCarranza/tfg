from peewee import *

db = MySQLDatabase('dw4mysql', user='dw4mysql', password='dw4mysql', charset='utf8mb4')


class BaseModel(Model):
    class Meta:
        database = db

