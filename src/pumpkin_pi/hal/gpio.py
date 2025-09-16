from gpiozero import LED, Device
from gpiozero.pins.native import NativeFactory
Device.pin_factory = NativeFactory()

class Gpio:
    def __init__(self, pin:int):
        self.led = LED(pin)
    def on(self): self.led.on()
    def off(self): self.led.off()
