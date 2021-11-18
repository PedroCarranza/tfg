import psutil
import os
import datetime

from cassandra.cluster import Cluster

session = Cluster(['127.0.0.1']).connect('dw4cassandra')
rows = session.execute("SELECT * from product limit 10")


class NoSqlExecute:
    def __init__(self, query=""):
        self.query = query

    def run(self):
        read_begin = psutil.disk_io_counters().read_bytes
        begin = datetime.datetime.now()
        session.execute(self.query)
        end = datetime.datetime.now()
        read_end = psutil.disk_io_counters().read_bytes
        return end-begin, read_end-read_begin
