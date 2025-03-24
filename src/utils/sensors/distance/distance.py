from src.lib.sensors.sensor import Sensor

class DistanceSensor(Sensor):
    def __init__(self,name:str, config:dict) -> None:
        super().__init__(name, sensor_type="Distance")
        self.config = config
        self._sensor = None
        self._read_range = None
        self._units = config['units']
        self._conversion_factor = 1
        
        match(config['driver']):
            case "JSN-SR04T":
                from src.lib.sensors.distance.jsnsr04t import JSNSR04T
                self._sensor = JSNSR04T(config['trigger_pin'], config['echo_pin'], config['units'])
                self._read_range_raw = self._sensor.read_range

            case "TR-EVO-MINI":
                from src.lib.sensors.distance.tr_evo_mini import EvoMini
                self._sensor = EvoMini(tx_pin=config['tx_pin'], rx_pin=['rx_pin'])
                self._read_range_raw = self._sensor.read_range
            
            case _:
                raise ValueError(f"Unsupported distance sensor driver: {config['driver']}")
            
            
        if self._units != self._sensor.BASE_UNITS:
            from src.lib.math.conversion import find_length_conversion
            self._conversion_factor = find_length_conversion(self._units, self._sensor.BASE_UNITS)
            
    def read_range(self):
        return self._read_range() * self._conversion_factor
        
# def distance_sensor(sensor:dict):
#     match sensor['driver']:
#         case "JSN-SR04T":
#             from src.lib.sensors.distance.jsnsr04t import JSNSR04T
#             return JSNSR04T(sensor['trigger_pin'], sensor['echo_pin'], sensor['units'])
        
        # case "TR-EVO-MINI":
            # from src.lib.sensors.distance.tr_evo_mini import TR_EVO_MINI
            # return TR_EVO_MINI(sensor['']