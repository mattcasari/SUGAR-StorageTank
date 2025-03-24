from .distance.distance import DistanceSensor


def create_distance_sensor(sensor:dict) -> DistanceSensor:
    return DistanceSensor(sensor['name'], sensor['config'])
    


# def DistanceSensor(sensor:dict) -> object:
#     if sensor['type'] == 'Distance':
#         from src.lib.sensors.distance.distance import distance_sensor
#         return distance_sensor(sensor)