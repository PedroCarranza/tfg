import psutil
import datetime
from cassandra.cluster import Cluster


class NoSqlExecute:
    def __init__(self, spark, query=""):
        self.session = Cluster(['127.0.0.1']).connect(keyspace='dw4cassandra')
        self.spark = spark
        self.query = query

    def run(self):
        read_begin = psutil.disk_io_counters().read_bytes
        begin = datetime.datetime.now()
        self.spark.sql(self.query).show(0, False)
        end = datetime.datetime.now()
        read_end = psutil.disk_io_counters().read_bytes
        return end-begin, read_end-read_begin
