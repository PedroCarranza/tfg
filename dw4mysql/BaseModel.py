from peewee import *

db = MySQLDatabase('dw4mysql', user='dw4mysql', password='dw4mysql', charset='utf8mb4')

# Arrumar tudo aqui
def create_tables():
    with db:
        db.create_tables()

# Arrumar tudo aqui
@app.before_request
def before_request():
    db.connect()

# Arrumar tudo aqui
@app.after_request
def after_request(response):
    db.close()
    return response


class BaseModel(Model):
    class Meta:
        database = db

