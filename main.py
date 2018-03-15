# Archivo principal MAIN
import machine
import time
from machine import Pin

#trigger en D5
trigger = Pin(14, mode=Pin.OUT, pull=None)
#echo en D6
echo = Pin(12, mode=Pin.IN, pull=None)
#inicia el trigger
trigger.value(1)

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
	# Velocidad de sonido a 20°C a 0msnm 343,2 m/s
	dist = pulso * 0.01716
	print("Distancia: ", dist,"cm")

# imprime valores cada segundo
while True:
	sensor_values()	
	time.sleep(1)