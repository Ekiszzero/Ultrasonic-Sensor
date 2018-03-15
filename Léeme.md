# Ultrasonic-Sensor
Esta es una versión en español sobre cómo utilizar un sensor HC-SR04 con NodeMCU (ESP8266)

# Elementos
Para conseguir mediciones satisfactorias se requiere alimentar el sensor HC-SR04 con 5 voltios, para ellos existen varias opciones. Sin embargo, en éste instructivo se utilizó un elevador de voltaje.

- NodeMCU
- Sensor ultrasónico HC-SR04
- Elevador de voltaje MT3608
- Cables jumpers
- Protoboard
- Resistor de 1kΩ

# Notas

- Si se obtienen medidas extrañas negativas, probablemente el sensor no esta recibiendo/emitiendo la señal adecuada, revisar la alimentación al HC-SR04, asegurarse que sean 5 voltios.

- HC-SR04 es distinto al HC-SR04+, éste último trabaja con 3.3V directamente mientras que el primero requiere 5V para su correcto funcionamiento.

- Para mejor comprensión, revisar el diagrama adjunto.
