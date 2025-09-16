from gpiozero import Device
from gpiozero.pins.mock import MockFactory
Device.pin_factory = MockFactory()

class Gpio:
    def __init__(self, pin:int):
        self.state = False
    def on(self): self.state = True
    def off(self): self.state = False
