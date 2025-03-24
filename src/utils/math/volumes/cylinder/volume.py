from ..generic.generic import GenericVolume

import math


class Volume(GenericVolume):
    def __init__(self, max_height: float, diameter: float):
        self._radius = diameter / 2
        super().__init__(max_height)

    def calculate_volume(self, depth: float) -> float:
        if depth < 0.0:
            raise ValueError(f"Depth must be non-negative.  Depth was {depth}")
        if depth > self.max_height:
            raise ValueError(
                f"Depth must not exceed max_height {self.max_height}.  Depth was {depth}"
            )
        return self._cylinder_volume(depth)

    def _cylinder_volume(self, height: float):
        # V=πr2h/3
        return math.pi * (self._radius**2) * height
