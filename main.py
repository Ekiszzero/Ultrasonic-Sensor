# Archivo principal MAIN
import machine
import time
import sys
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
	dist = round(pulso * 0.01716, 2)
	a=0
	
	while dist<2 or dist>400:
			trigger.value(1)
			time.sleep_us(10)
			trigger.value(0)
			pulso = machine.time_pulse_us(echo, 1, 30000)
			dist = round(pulso * 0.01716, 2)
			a+=1
			if a==2:
				sys.stdout.write('--> midiendo..')
			elif a>2:
				sys.stdout.write('.')

	if a!=0:
		print("")

	print("Distancia: ", dist,"cm")

# imprime valores cada segundo
while True:
	sensor_values()	
	time.sleep(2)
