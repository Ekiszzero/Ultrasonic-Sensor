# Archivo principal MAIN
import machine
import time
from machine import Pin


trigger = Pin(14, mode=Pin.OUT, pull=None)
trigger.value(1)
echo = Pin(12, mode=Pin.IN, pull=None)

def sensor_values():
	trigger.value(0)
	time.sleep_us(2)
	# inicia el pulso de 10us
	trigger.value(1)
	time.sleep_us(10)
	trigger.value(0)
	# activar echo
	pulso = machine.time_pulse_us(echo, 1, 30000)
	# Calcular distancia
	dist = (pulso / 2) / (29.1)
	print("Distance", " - ", dist)


# prints values every second
while True:
	sensor_values()	
	time.sleep(1)