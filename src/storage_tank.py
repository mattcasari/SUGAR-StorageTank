import math
from time import sleep_ms
from src.utils.math.volumes.generic.generic import GenericVolume
from src.utils.math.conversion import in3_to_gallons


class StorageTank:
    def __init__(
        self,
        get_distance: function,
        upper_tank: GenericVolume,
        lower_tank: GenericVolume,
        mounted_distance: float,
    ):
        """_summary_

        Args:
            get_distance (function): Function that reads the distance sensor distance
            mounted_distance (float): Distance sensor is mounted above top of tank (in)
        """
        print("Init TANK")
        print(f"Mounted distance passed: {mounted_distance} in")
        self.get_distance = get_distance
        self._mounted_distance = mounted_distance
        self._lower_tank = lower_tank
        self._upper_tank = upper_tank
        self._max_height = self._lower_tank.max_height + self._upper_tank.max_height
        self._max_volume = self._lower_tank.max_volume + self._upper_tank.max_volume

        print(f"Mounted height = {self._mounted_distance} in")
        print(f"Total Max Height = {self._max_height} in")
        print(f"Max volume calculated: {self._max_volume} in")
        print(f"Max volume calculated: {in3_to_gallons(self._max_volume)} gallons")

    def read_tank(self):
        retry_cnt = 0
        while retry_cnt < 10:
            try:
                (volume, depth) = self._get_volume()
                print(f"Volume: {volume:.1f} gallons")
                return (volume, depth)
            except ValueError as e:
                print(f"Error in read.  Message was: {e}")
                retry_cnt += 1
                print(f"Retrying... attempt {retry_cnt}")
                sleep_ms(250)
                return (0, 0)

    def _get_volume(self) -> tuple[float, float]:
        """Calculate the volume

        Returns:
            tuple[float,float]: volume (gallons), depth(inches)
        """
        print("\nGet volume...")
        distance = self.get_distance()
        depth = self._mounted_distance + self._max_height - distance
        print(f"Dist = {distance:.2f} in, Depth = {depth:.2f}in")

        if depth < 0.0:
            return (0, 0)

        volume = self._calculate_combined_volume(depth=depth)

        if volume < 0.0:
            return (0, 0)

        if volume < self._max_volume:
            return (in3_to_gallons(volume), depth)

        return (in3_to_gallons(self._max_volume), self._max_height)

    def _calculate_combined_volume(self, depth: float) -> float:
        volume = 0.0
        if depth > self._lower_tank.max_height:
            volume += self._upper_tank.calculate_volume(depth - self._lower_tank.max_height)

        volume += self._lower_tank.calculate_volume(depth)

        return volume
