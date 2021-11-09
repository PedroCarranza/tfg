import psutil
from openpyxl import *
from concurrent.futures import ThreadPoolExecutor
from computerUsage import ComputerUsage
from sqlExecute import SqlExecute

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
                    print(new_thread.result())
                finally:
                    usage.keep_measuring = False
                    cpu_usage, ram_usage, swap_usage = main_thread.result()
                    print(cpu_usage)
                    print(ram_usage)
                    print(swap_usage)
            else:
                break
