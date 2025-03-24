class Sensor:
    def __init__(self, name:str, sensor_type:str) -> None:
        self._name = name
        self._type = sensor_type
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type