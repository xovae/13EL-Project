import machine
import utime
from machine import Pin, Timer

led = machine.Pin('LED', machine.Pin.OUT)
led.high()

#leftMotor = machine.Pin(16, machine.Pin.OUT) # bottom pin
class motor:
    def forward(this):
        this.posTrans2.low()
        this.negTrans2.low()
        this.posTrans1.high()
        this.negTrans1.high()

    def backwards(this):
        this.posTrans1.low()
        this.negTrans1.low()
        this.negTrans2.high()
        this.posTrans2.high()

    def __init__(this, posTrans1, posTrans2, negTrans1, negTrans2):
        this.posTrans1 = machine.Pin(posTrans1, machine.Pin.OUT)
        this.posTrans2 = machine.Pin(posTrans2, machine.Pin.OUT)
        this.negTrans1 = machine.Pin(negTrans1, machine.Pin.OUT)
        this.negTrans2 = machine.Pin(negTrans2, machine.Pin.OUT)

leftMotor = motor(15, 14, 13, 12)
rightMotor = motor(16, 17, 18, 19)

while True:
    leftMotor.forward()
    rightMotor.forward()
