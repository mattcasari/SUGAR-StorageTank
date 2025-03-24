from ..generic.generic import GenericVolume


class Volume(GenericVolume):
    def __init__(self, max_height: float, width: float, depth: float):
        self._width = width
        self._depth = depth
        super().__init__(max_height)

        print(self)

    def calculate_volume(self, depth) -> float:
        if depth < 0.0:
            raise ValueError(f"Depth must be non-negative.  Depth was {depth}")
        if depth > self.max_height:
            raise ValueError(
                f"Depth must not exceed max_height {self.max_height}.  Depth was {depth}"
            )
        return self._box_volume(depth)

    def _box_volume(self, height: float):
        # volume = Width * Depth * Height
        return self._width * self._depth * height
