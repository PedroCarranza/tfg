import psutil
from peewee import *
import datetime

db = MySQLDatabase('dw4mysql', user='dw4mysql', password='dw4mysql', charset='utf8mb4')


class SqlExecute:
    def __init__(self, sql=""):
        self.sql = sql

    def run(self):
        read_begin = psutil.disk_io_counters().read_bytes
        begin = datetime.datetime.now()
        db.execute_sql(self.sql)
        end = datetime.datetime.now()
        read_end = psutil.disk_io_counters().read_bytes
        return end-begin, read_end-read_begin
