from machine import Pin, time_pulse_us
import time


class JSNSR04T:
    BASE_UNITS = 'cm'
    def __init__(self, trigger_pin: int, echo_pin: int, units: str = 'in'):
        self._trigger_pin = Pin(trigger_pin, Pin.OUT)
        self._echo_pin = Pin(echo_pin, Pin.IN)

    def read_range(self):
        time.sleep_ms(10)
        # Trigger a measurement
        self._trigger_pin.value(0)
        time.sleep_us(2)
        self._trigger_pin.value(1)
        time.sleep_us(10)

        self._trigger_pin.value(0)
        pulse = time_pulse_us(self._echo_pin, 1, 50000)

        # Read the pulse

        print(f"{pulse=}")

        # Convert the pulse to distance in cm
        distance = pulse * 0.0343 / 2

        if distance > 600:
            distance = 600

        if distance < 0:
            distance = 0

        return distance # Returns cm


