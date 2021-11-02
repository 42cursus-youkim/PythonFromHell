class Celsius:
    def __init__(self, temperature : int = 4) -> None:
        self.temperature : int = temperature
    
    def to_fahrenheit(self) -> int:
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self) -> int:
        print("get value")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value : int):
        if value < -273:
            raise ValueError("Temperature error")
        print("set value")
        self._temperature = value


c = Celsius()
print("----------")
print(c.temperature)
print("----------")
print(c.to_fahrenheit())
print("----------")
c.temperature = 300
print("----------")
c.temperature = -700