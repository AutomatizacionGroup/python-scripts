
from serial import Serial
import time

port = 'COM3'

if __name__ == '__main__':
    ser = Serial(port, 115200)
    ser.flush()
    date = time.strftime("%Y%m%d")
    log = open(date + '.log', 'a')

    while True:
        if ser.in_waiting > 0:
            line = time.strftime("%Y/%m/%d-%H:%M:%S") + ' | '
            line += ser.readline().decode().rstrip()
            line += '\n'
            log.write(line)
            print(line)

            if date != time.strftime("%Y%m%d"):
                date = time.strftime("%Y%m%d")
                log.close()
                log = open(date + '.log', 'a')
    
    log.close()