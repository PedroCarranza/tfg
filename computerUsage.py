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
        self.cpu_monitored = []
        self.ram_monitored = []
        self.swap_monitored = []

        cpu_measured = ram_measured = swap_measured = 0
        quantity = self.quantity_count
        while quantity > 0:
            cpu_measured += ps.cpu_percent(interval=self.time_interval)
            ram_measured += ps.virtual_memory().used
            swap_measured += ps.swap_memory().used
            quantity -= 1

        self.cpu_base = cpu_measured/self.quantity_count
        self.ram_base = ram_measured/self.quantity_count
        self.swap_base = swap_measured/self.quantity_count

    def run(self):
        while self.keep_measuring:
            cpu_mes = ps.cpu_percent(interval=self.time_interval)
            ram_mes = ps.virtual_memory().used
            swap_mes = ps.swap_memory().used

            self.cpu_monitored.append(round(cpu_mes - self.cpu_base, 4))
            self.ram_monitored.append(round(ram_mes - self.ram_base, 4))
            self.swap_monitored.append(round(swap_mes - self.swap_base, 4))

        return self.cpu_monitored, self.ram_monitored, self.swap_monitored

