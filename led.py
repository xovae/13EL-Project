from machine import Pin, Timer
led = Pin("LED", Pin.OUT)
'timOn = Timer()
'timOff = Timer()
'def tick(timer):
'    global led
'    led.off()
'def tick2(timer):
'    global led
'    led.on()

'timOn.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
'timOff.init(freq= 1.25, mode=Timer.PERIODIC, callback=tick2)
led.on()

class motor:
    def forward(this):
        this.TransPosF.high()
        this.TransNegF.high()
        this.TransPosB.low()
        this.TransNegB.low()
        
    def backwards(this):
        this.TransPosB.high()
        this.TransNegB.high()
        this.TransPosF.low()
        this.TransPosF.low()
        
    def init(this, TransPosF, TransPosB, TransNegF, TransNegB)
        this.TransPosF = machine.Pin(TransPosF, machine.Pin.OUT)
        this.TransPosB = machine.Pin(TransPosB, machine.Pin.OUT)
        this.TransNegF = machine.Pin(TransNegF, machine.Pin.OUT)
        this.TransNegB = machine.Pin(TransNegB, machine.Pin.OUT)
    
leftMotor = motor(15, 14, 13, 12)
rightMotor = motor(16, 17, 18, 19)

