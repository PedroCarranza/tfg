from peewee import *
from dw4mysql.BaseModel import BaseModel


class Review(BaseModel):
    id = UUIDField(primary_key=True)
    score = IntegerField()
    comment_title = CharField()
    comment_message = CharField()
    creation_date = CharField()
    answer_timestamp = CharField()


