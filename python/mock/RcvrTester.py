import socket
import time
import io
import csv
import sys
import logging


def create_socket_client():
    logging.basicConfig(level=logging.DEBUG, filename="error.log")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 7777
    host = 'localhost'
    s.bind((host, port))
    while True:
        try:
            data, server = s.recvfrom(4080)
            if not data:
                break
            csv_data = csv.reader(io.StringIO(data.decode('utf-8')))
            data_values = next(csv_data)
            aoa = data_values[0]
            nx = data_values[1]
            ny = data_values[2]
            nz = data_values[3]
            vv = data_values[4]
            ias = data_values[5]
            balt = data_values[6]
            process_data(aoa, nx, ny, nz,vv, ias, balt)
        except socket.error as err:
            print('Connection error...')
            logging.error('Connection error...', exc_info=True)
            time.sleep(5)  # Wait for 5 seconds before next attempt


def process_data(aoa: str, nx: str, ny: str, nz: str, vv: str, ias: str, balt: str):
    aoa = float(aoa)
    nx = float(nx)
    ny = float(ny)
    nz = float(nz)
    vv = int(float(vv) * 196.85)
    ias = int(float(ias) * 1.94384)
    balt = int(float(balt) * 3.281)
    sys.stdout.write('\rAoA: {aoa} | Nx: {nx} G | Ny {ny} G | Nz {nz} G | VV: {vv} ft/min | IAS : {ias} kts | BAlt: {balt} ft'.format(aoa=aoa, nx=nx, ny=ny, nz=nz, vv=vv, ias=ias, balt=balt))
    sys.stdout.flush()


if __name__ == "__main__":
    create_socket_client()
