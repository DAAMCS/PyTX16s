# PyTX16s
Python lib to interact with `RadioMaster TX16s`.
---
_Probably works on other RC`s, needs to be tested._


## Installation
The most important thing is that the [HID API](https://github.com/libusb/hidapi) is installed in the system.
For Windows, it is enough to download the `hidapi-win.zip` archive of the [latest](https://github.com/libusb/hidapi/releases/latest) version and transfer the DLL file to the Windows\System32 folder.
For other systems, there are instructions in the repository of the driver itself.

Python 3.x and [`Python HID Api`](https://github.com/apmorton/pyhidapi)(already in dependencies) is required (tested on Python 3.11 and newer).

```
pip install PyTX16s
```
also poetry can be used to work with sources:

```
poetry install
```

## Basic Usage
Connect controller to PC, then instantiate a `Joystick` class. It must detect your controller automatically, otherwise - it will be prompt provided with connected devices list in your shell and you will be able to choose it manually.

```python
import logging
from pytx16s import Joystick

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

device = Joystick()

while True:
    print(device.get_device_report())
```

## Package distribution notes
_There are just notes to self for updating the pypi distribution_
* Update the release number in `pyproject.toml` and commit to repo.
* Draft a new release in github using the same release number.
* Run `poetry build`
* Publish the distribution to pypi: `poetry publish`
