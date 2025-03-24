from ..generic.generic import GenericVolume

import math


class Volume(GenericVolume):
    def __init__(self, max_height: float, width: float, depth: float):
        """Initializes the volume to be a half horizontal elliptical container.

        ----------------    -----
        (              )      |
         \            /       |
           (         )    max_height
             (     )          |
              -----         -----

        Args:
            max_height (float): the height from the bottom to the top of the container (half of an ellipse)
            width (float): Width of the container
            depth (float): Depth of the container
        """
        self._width = width
        self._depth = depth
        self._full_ellipse_height = max_height * 2
        super().__init__(max_height)

    def calculate_volume(self, depth: float) -> float:
        if depth < 0.0:
            raise ValueError(f"Depth must be non-negative.  Depth was {depth}")
        if depth > self.max_height:
            raise ValueError(
                f"Depth must not exceed max_height {self.max_height}.  Depth was {depth}"
            )
        return self._horizontal_half_ellipse_volume(depth)

    def _horizontal_half_ellipse_volume(self, height: float):
        # Vell_f = l x h X w/4 X [arccos(1-(2xf)/h) - (1-(2xf)/h) * sqrt((4xf)/h - (4xf^2)/h^2)]
        f = height
        h = self._full_ellipse_height

        vol = math.acos(1 - (2 * f) / h) - (1 - (2 * f) / h) * math.sqrt(
            (4 * f) / h - (4 * f**2) / h**2
        )
        vol *= h * self._depth * self._width / 4
        return vol
