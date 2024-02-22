import socket
import time

from tests.TestDataGenerator import TestDataGenerator as Dg

host = "localhost"
port = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
generator = Dg()

try:
    while True:
        data_aoa = next(generator.generator_aoa)
        data_nx = next(generator.generator_nx)
        data_ny = next(generator.generator_ny)
        data_nz = next(generator.generator_nz)
        data_vvert = next(generator.generator_vvert)
        data_ias = next(generator.generator_ias)
        data_altBar = next(generator.generator_altBar)
        data = f'{data_aoa:.2f},{data_nx:.2f},{data_ny:.2f},{data_nz:.2f},{data_vvert:.1f},{data_ias:.1f},{data_altBar:.1f}'
        sock.sendto(data.encode('utf-8'), (host, port))
        time.sleep(.5)

except KeyboardInterrupt:
    print("Przerwano przez użytkownika.")

finally:
    sock.close()
