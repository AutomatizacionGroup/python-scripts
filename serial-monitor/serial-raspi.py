
from serial import Serial
import time
import paho.mqtt.client as mqtt

port = '/dev/ttyUSB0'
baud_rate = 115200

client = mqtt.Client()
client.connect("loacalhost", 1883, 60)
client.loop_start()
mqtt = True

if __name__ == '__main__':
    #inicia Serial
    ser = Serial(port, baud_rate)
    ser.flush()

    # Obtiene fecha inicial
    date = time.strftime("%Y%m%d")

    # Ciclo infinito
    while True:
        # Espera hasta que el serial reciba informacion
        if ser.in_waiting > 0:
            # Abre archivo Log
            log = open('logs/' + date + '.log', 'a')

            # Agrega hora
            line = time.strftime("%H:%M:%S") + ' | '
            
            # Lee la linea del Serial
            line += ser.readline().decode().rstrip()
            line += '\n'
            
            # Escribe en el log
            log.write(line)
            
            #imprime
            print(line)

            if mqtt:
                #publica en mqtt
                mqttc.publish("/serial", line)

            log.close()
            # Si la fecha inicial no coincide con la nueva fecha tomada
            # abre un nuevo archivo con la nueva fecha
            if date != time.strftime("%Y%m%d"):
                date = time.strftime("%Y%m%d")
    
    log.close()