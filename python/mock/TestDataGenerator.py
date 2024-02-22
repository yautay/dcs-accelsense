import math
from typing import List


class TestDataGenerator:
    def __init__(self):
        self.aoa = [17.5, 12.5]
        self.nx = [1, 0]
        self.ny = [4.5, 2.5]
        self.nz = [1, 0]
        self.vvert = [3500, 1500]
        self.ias = [375, 525]
        self.altBar = [5900, 6100]
        self.generator_aoa = self.data_generator(self.aoa)
        self.generator_nx = self.data_generator(self.nx)
        self.generator_ny = self.data_generator(self.ny)
        self.generator_nz = self.data_generator(self.nz)
        self.generator_vvert = self.data_generator(self.vvert)
        self.generator_ias = self.data_generator(self.ias)
        self.generator_altBar = self.data_generator(self.altBar)

    @staticmethod
    def data_generator(params: List[float]):
        x = 0
        while True:
            data = params[0] * math.sin(x) + params[1]
            yield data
            x += 0.01
