import Adafruit_BBIO.GPIO as GPIO

# Pins dont exist in CPython so...lets make our own!
class Pin:
    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1
    PULL_NONE = 0
    PULL_UP = 1
    PULL_DOWN = 2
    
    id = None
    _value = LOW
    _mode = IN
    
    def __init__(self, pin_name):
        self.id = pin_name

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other

    def init(self, mode=IN, pull=None):
        if mode != None:
            if mode == self.IN:
                self._mode = self.IN
                GPIO.setup(self.id, GPIO.IN)
            elif mode == self.OUT:
                self._mode = self.OUT
                GPIO.setup(self.id, GPIO.OUT)
            else:
                raise RuntimeError("Invalid mode for pin: %s" % self.id)
        if pull != None:
            if self._mode != self.IN:
                raise RuntimeError("Cannot set pull resistor on output")
            if pull == self.PULL_UP:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            elif pull == self.PULL_DOWN:
                GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            else:
                raise RuntimeError("Invalid pull for pin: %s" % self.id)       

    def value(self, val=None):
        if val != None:
            if val == self.LOW:
                self._value = val
                GPIO.output(self.id, val)
            elif val == self.HIGH:
                self._value = val
                GPIO.output(self.id, val)
            else:
                raise RuntimeError("Invalid value for pin")
        else:
            return GPIO.input(self.id)

P8_13 = Pin('P8_13')
P8_19 = Pin('P8_19')

P9_12 = Pin('P9_12')


USR0 = Pin('USR0')
USR1 = Pin('USR1')
USR2 = Pin('USR2')
USR3 = Pin('USR3')

# ordered as spiId, sckId, mosiId, misoId
spiPorts = ()

# ordered as uartId, txId, rxId
uartPorts = (
    (),
)

i2cPorts = (
    (),
)

