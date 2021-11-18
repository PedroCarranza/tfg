import psutil
from openpyxl import *
from openpyxl.styles import *
from concurrent.futures import ThreadPoolExecutor
from computerUsage import ComputerUsage
from sqlExecute import SqlExecute

wb_destination = Workbook()
ws = wb_destination.active
ws.title = "Mysql and Cassandra Queries"
ws.merge_cells('A1:E1')
ws.merge_cells('F1:J1')
font = Font(name="Times", size=14)
ws['A1'] = "Mysql"
ws['A2'] = ws['F2'] = "Time used"
ws['B2'] = ws['G2'] = "Bytes used"
ws['C2'] = ws['H2'] = "CPU used"
ws['D2'] = ws['I2'] = "RAM used"
ws['E2'] = ws['J2'] = "SWAP used"
ws['F1'] = "Cassandra"

wb = load_workbook(filename="geradorConsulta.xlsx", data_only=True)
sheet = wb.active

with ThreadPoolExecutor() as executor:
    usage = ComputerUsage()
    sqlExec = SqlExecute()

    for j in range(4, sheet.max_column):
        for i in range(4, sheet.max_row):
            if sheet.cell(row=i, column=j).value is not None:
                sqlExec.sql = sheet.cell(row=i, column=j).value
                usage.start()
                main_thread = executor.submit(usage.run)
                try:
                    new_thread = executor.submit(sqlExec.run)
                    time_spent, bytes_usage = new_thread.result()
                finally:
                    usage.keep_measuring = False
                    cpu_usage, ram_usage, swap_usage = main_thread.result()
                    print(time_spent, bytes_usage, cpu_usage, ram_usage, swap_usage)
            else:
                break

wb_destination.save(filename="query_results.xlsx")