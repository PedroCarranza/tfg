import time

import psutil as ps


class ComputerUsage:
    def __init__(self, time_interval=0.1, quantity_count=100):
        self.time_interval = time_interval
        self.quantity_count = quantity_count
        self.cpu_monitored = [0]
        self.ram_monitored = [0]
        self.swap_monitored = [0]
        self.keep_measuring = False
        self.cpu_base = 0
        self.ram_base = 0
        self.swap_base = 0

    def start(self):
        self.keep_measuring = True
        self.cpu_monitored = [0]
        self.ram_monitored = [0]
        self.swap_monitored = [0]

        time.sleep(10)

        self.cpu_base = ps.cpu_percent(interval=self.time_interval)
        self.ram_base = ps.virtual_memory().used
        self.swap_base = ps.swap_memory().used

    def run(self):
        while self.keep_measuring:
            cpu_mes = ps.cpu_percent(interval=self.time_interval)
            ram_mes = ps.virtual_memory().used
            swap_mes = ps.swap_memory().used

            self.cpu_monitored.append(round(cpu_mes - self.cpu_base, 4))
            self.ram_monitored.append(round(ram_mes - self.ram_base, 4))
            self.swap_monitored.append(round(swap_mes - self.swap_base, 4))

            self.cpu_base = cpu_mes
            self.ram_base = ram_mes
            self.swap_base = swap_mes

        return self.cpu_monitored, self.ram_monitored, self.swap_monitored

