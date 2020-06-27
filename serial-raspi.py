
from serial import Serial
import time

port = 'COM3'
baud_rate = 115200

if __name__ == '__main__':
    #inicia Serial
    ser = Serial(port, baud_rate)
    ser.flush()

    # Obtiene fecha inicial
    date = time.strftime("%Y%m%d")

    # Abre archivo Log
    log = open(date + '.log', 'a')

    # Ciclo infinito
    while True:
        # Espera hasta que el serial reciba informacion
        if ser.in_waiting > 0:
            # Agrega hora
            line = time.strftime("%H:%M:%S") + ' | '
            # Lee la linea del Serial
            line += ser.readline().decode().rstrip()
            line += '\n'
            # Escribe en el log
            log.write(line)
            #imprime
            print(line)

            # Si la fecha inicial no coincide con la nueva fecha tomada
            # abre un nuevo archivo con la nueva fecha
            if date != time.strftime("%Y%m%d"):
                date = time.strftime("%Y%m%d")
                log.close()
                log = open(date + '.log', 'a')
    
    log.close()