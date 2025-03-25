from src.utils.sensors.sensor import Sensor


class DistanceSensor(Sensor):
    def __init__(self, name: str, config: dict) -> None:
        super().__init__(name, sensor_type="Distance")
        self.config = config
        self._sensor = None
        self._read_range_raw = lambda: -1
        self._units = config["units"]
        self._conversion_factor = 1
        print(config)
        if config["driver"] == "JSN-SR04T":
            from src.utils.sensors.distance.jsnsr04t import JSNSR04T

            self._sensor = JSNSR04T(
                config["Pin"]["trigger_pin"], config["Pin"]["echo_pin"], config["units"]
            )
            self._read_range_raw = self._sensor.read_range

        elif config["driver"] == "TR-EVO-MINI":
            from src.utils.sensors.distance.tr_evo_mini import EvoMini

            self._sensor = EvoMini(tx_pin=config["Pin"]["tx_pin"], rx_pin=["Pin"]["rx_pin"])
            self._read_range_raw = self._sensor.read_range

        else:
            raise ValueError(f"Unsupported distance sensor driver: {config['driver']}")
        print(self._sensor)
        if self._units != self._sensor.BASE_UNITS:
            from src.utils.math.conversion import find_length_conversion

            self._conversion_factor = find_length_conversion(
                unit_to=self._units, unit_from=self._sensor.BASE_UNITS
            )
            print(f"Conversion Factor = {self._conversion_factor}")

    def read_range(self):
        return self._read_range_raw() * self._conversion_factor
