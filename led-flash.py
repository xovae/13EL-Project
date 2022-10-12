from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)

while True:
    pin.toggle()
    sleep(1)
    
# timOn = Timer()
# timOff = Timer()
# def tick(timer):
#     global led
#     led.off()
# def tick2(timer):
#     global led
#     led.on()
# timOn.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
# timOff.init(freq= 1.25, mode=Timer.PERIODIC, callback=tick2)