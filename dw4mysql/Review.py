from peewee import *
from dw4mysql.BaseModel import BaseModel


class Review(BaseModel):
    id = UUIDField(primary_key=True)
    review_id = UUIDField(null=False)
    score = IntegerField(null=False)
    comment_title = CharField(null=False)
    comment_message = CharField(null=False)
    creation_date = CharField(null=False)
    answer_timestamp = CharField(null=False)

    class Meta:
        db_table = 'review'


Review.create_table()


