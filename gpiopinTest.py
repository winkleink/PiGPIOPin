from PiGPIOPin import *
from gpiozero import LED
from time import sleep

red = LED(PIN11)

while True:
    print ("PIN17 is " + str(PIN11))
    red.on()
    sleep(1)
    red.off()
    sleep(1)
