# PCF8574 simulation

This is a Python library you can use when working with the [pcf8574 library](https://pypi.org/project/pcf8574/).
It works exactly the same as the original library, but is intended for testing purposes when the I²C-Bus hardware is not connected.

## Installation

```bash
pip install pcf8574_simulation
```


## Usage

You have different options to use this as an alternative to the original library.

For example, you can import the correct library depending on which is installed on your system:

```python
try:
    from pcf8574 import PCF8574, IOPort
except ImportError:
    print("No I2C bus package found. Starting simulation")
    from pcf8574_simulation import PCF8574, IOPort
```

Then you can use the PCF8574 class as usual:

```python
pcf = PCF8574(1, 0x20)
print(pcf.port)  # [True, True, True, True, True, True, True, True]
pcf.port[0] = False
print(pcf.port[0])  # False
```

