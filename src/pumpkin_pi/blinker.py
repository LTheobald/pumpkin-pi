from __future__ import annotations

import sys
import time
from dataclasses import dataclass
from typing import Optional


def _try_import_gpiozero():
    try:
        from gpiozero import LED  # type: ignore

        return LED
    except Exception:
        return None


LEDClass = _try_import_gpiozero()


@dataclass
class Blinker:
    """Blink an LED on a Raspberry Pi, with simulation fallback.

    If gpiozero is available and simulation is not forced, uses a real
    LED on the provided GPIO pin. Otherwise, prints simulated blink events.
    """

    pin: int = 17
    simulate: bool = False

    def __post_init__(self) -> None:
        self._use_gpio = (LEDClass is not None) and (not self.simulate)
        self._led = None
        if self._use_gpio:
            try:
                self._led = LEDClass(self.pin)  # type: ignore[call-arg]
            except Exception as e:  # Hardware errors or misconfiguration
                # Fall back to simulation if hardware cannot be initialized
                print(
                    f"[pumpkin-pi] GPIO init failed ({e}); using simulation.",
                    file=sys.stderr,
                )
                self._use_gpio = False
                self._led = None

    @property
    def is_simulated(self) -> bool:
        return not self._use_gpio

    def blink(self, count: int = 3, interval: float = 0.5) -> None:
        """Blink the LED or simulate.

        - count: number of on/off cycles
        - interval: seconds between on/off transitions
        """
        if count < 0:
            raise ValueError("count must be >= 0")
        if interval < 0:
            raise ValueError("interval must be >= 0")

        if self._use_gpio and self._led is not None:
            for i in range(count):
                self._led.on()
                time.sleep(interval)
                self._led.off()
                time.sleep(interval)
        else:
            for i in range(count):
                print(f"[pumpkin-pi] Simulated LED on (pin {self.pin}) [{i+1}/{count}]")
                time.sleep(interval)
                print(
                    f"[pumpkin-pi] Simulated LED off (pin {self.pin}) [{i+1}/{count}]"
                )
                time.sleep(interval)
