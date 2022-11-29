import machine
import utime
from time import sleep

led = machine.Pin('LED', machine.Pin.OUT)
led.high()

buzzer = machine.Pin(21, machine.Pin.OUT)
buzzer.high()
sleep(1)
buzzer.low()

class motor:
    def __init__(this, posTrans1, posTrans2, negTrans1, negTrans2):
        this.posTrans1 = machine.Pin(posTrans1, machine.Pin.OUT)
        this.posTrans2 = machine.Pin(posTrans2, machine.Pin.OUT)
        this.negTrans1 = machine.Pin(negTrans1, machine.Pin.OUT)
        this.negTrans2 = machine.Pin(negTrans2, machine.Pin.OUT)
        
def forward(this):
        this.posTrans2.low()
        this.negTrans2.low()
        this.posTrans1.high()
        this.negTrans1.high()

def backward(this):
        this.posTrans1.low()
        this.negTrans1.low()
        this.negTrans2.high()
        this.posTrans2.high()

leftMotor = motor(15, 14, 12, 13)
rightMotor = motor(16, 17, 19, 18)

while True:
    forward(leftMotor)
    forward(rightMotor)
    sleep(2)
    backward(leftMotor)
    backward(rightMotor)
    sleep(2)
    # leftMotor.forward()
    # rightMotor.forward()
