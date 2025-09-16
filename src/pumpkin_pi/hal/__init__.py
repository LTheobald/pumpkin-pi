import os
if os.getenv("USE_MOCK_GPIO", "1") == "1":
    from .gpio_mock import Gpio
else:
    from .gpio import Gpio
