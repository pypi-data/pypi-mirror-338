from typing import List, Iterator


class IOPort:
    """
    Represents the simulated PCF8574 IO port as a list of boolean values.
    """
    def __init__(self, pcf8574: 'PCF8574') -> None:
        self.pcf8574 = pcf8574

    def __setitem__(self, key: int, value: bool) -> None:
        self.pcf8574.set_output(key, value)

    def __getitem__(self, key: int) -> bool:
        return self.pcf8574.get_pin_state(key)

    def __repr__(self) -> str:
        return repr(self.pcf8574.state)

    def __len__(self) -> int:
        return 8

    def __iter__(self) -> Iterator[bool]:
        for i in range(8):
            yield self[i]

    def __reversed__(self) -> Iterator[bool]:
        for i in range(8):
            yield self[7 - i]


class PCF8574:
    """
    A software representation of a PCF8574 IO expander chip, with WebSocket control.
    Useful for testing your software without your hardware.
    """
    def __init__(self, i2c_bus_no: int, address: int) -> None:
        self.bus_no: int = i2c_bus_no
        self.address: int = address
        self.state: List[bool] = [True] * 8  # Simulate the 8 pins

    def __repr__(self) -> str:
        return f"PCF8574(address=0x{self.address:02x})"

    @property
    def port(self) -> IOPort:
        return IOPort(self)

    @port.setter
    def port(self, value: List[bool]) -> None:
        assert len(value) == 8, "Port value must be a list of 8 booleans."
        self.state = value

    def set_output(self, output_number: int, value: bool) -> None:
        assert 0 <= output_number < 8, "Output number must be between 0 and 7"
        self.state[output_number] = value

    def get_pin_state(self, pin_number: int) -> bool:
        assert 0 <= pin_number < 8, "Pin number must be between 0 and 7"
        return self.state[pin_number]
