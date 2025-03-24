import pytest
from src.utils.math.volumes.cylinder.volume import Volume as CylinderVolume


def test_cone_volume_for_known_valid_volume():
    # Given: a set of cone dimensions with known volume
    diameter = 30
    height = 3.0
    expected_volume = 2120.58

    # When: The cylinder Volume object is created
    cylinder = CylinderVolume(height, diameter)

    # Then: The calculated total volume is correct
    assert cylinder.MAX_VOLUME == pytest.approx(expected_volume, abs=1e-2)


def test_cylinder_volume_level_for_known_level_volume():
    # Given: a set of cylinder dimensions and a known volume level
    diameter = 30
    height = 3.0
    level_height = 2.0
    expected_volume_level = 1413.72

    # When: The cylinder Volume object is created
    cylinder = CylinderVolume(height, diameter)

    # Then: The calculated level volume is correct
    assert cylinder.calculate_volume(level_height) == pytest.approx(
        expected_volume_level, abs=1e-2
    )


def test_cylinder_volume_level_returns_error_when_level_is_above_max():
    # Given: A set of cylinder dimensions and a level height > max height
    diameter = 30
    height = 3.0
    height = 3.0
    level_height = 3.01

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        cylinder = CylinderVolume(height, diameter)
        cylinder.calculate_volume(level_height)


def test_cylinder_volume_level_returns_error_when_level_is_less_than_zero():
    # Given: A set of cylinder dimensions and a level height < 0
    diameter = 30
    height = 3.0
    height = 3.0
    level_height = -1.0

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        cylinder = CylinderVolume(height, diameter)
        cylinder.calculate_volume(level_height)
