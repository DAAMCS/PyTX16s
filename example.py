import logging
from pytx16s import Joystick

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

device = Joystick()

while True:
    print(device.get_device_report())