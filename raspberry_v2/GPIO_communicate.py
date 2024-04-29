from gpiozero import LED, Button
from signal import pause

led = LED(21)
button = Button(16)

while True:
	if button.is_pressed:
		led.off()
	else:
		led.on() 
