from ..generic.generic import GenericVolume

import math


class Volume(GenericVolume):
    def __init__(self, max_height: float, diameter: float):
        self._radius_top = diameter / 2
        self._radius_bottom = 0.001
        self._angle = math.atan2(self._radius_top, max_height)
        super().__init__(max_height)

    def calculate_volume(self, depth: float) -> float:
        if depth < 0.0:
            raise ValueError(f"Depth must be non-negative.  Depth was {depth}")
        if depth > self.max_height:
            raise ValueError(
                f"Depth must not exceed max_height {self.max_height}.  Depth was {depth}"
            )
        return self._cone_volume(depth)

    def _cone_volume(self, height: float):
        # V=πr2h/3
        r_level = height * math.tan(self._angle)
        return math.pi * (r_level**2) * height / 3

    def _frustum_volume(self, height: float) -> float:
        # V = (1/3)πh(r1^2 + r2^2 + r1*r2)
        # Vff =(1/3)πf(R^2 + R*d_bot)
        return (
            (1 / 3)
            * math.pi
            * height
            * (
                self._radius_top**2
                + self._radius_top * self._radius_bottom
                + self._radius_bottom**2
            )
        )
