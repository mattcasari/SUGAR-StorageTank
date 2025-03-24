import pytest
from src.utils.math.volumes.cone.volume import Volume as ConeVolume


def test_cone_volume_for_known_valid_volume():
    # Given: a set of cone dimensions with known volume
    diameter = 30
    height = 3.0
    expected_volume = 706.9

    # When: The cone Volume object is created
    cone = ConeVolume(height, diameter)

    # Then: The calculated total volume is correct
    assert cone.MAX_VOLUME == pytest.approx(expected_volume, abs=1e-1)


def test_cone_volume_level_for_known_level_volume():
    # Given: a set of cone dimensions and a known volume level
    diameter = 30
    height = 3.0
    level_height = 2.0
    expected_volume_level = 209.5

    # When: The cone Volume object is created
    cone = ConeVolume(height, diameter)

    # Then: The calculated level volume is correct
    assert cone.calculate_volume(level_height) == pytest.approx(expected_volume_level, abs=1e-1)


def test_cone_volume_level_returns_error_when_level_is_above_max():
    # Given: A set of cone dimensions and a level height > max height
    diameter = 30
    height = 3.0
    height = 3.0
    level_height = 3.01

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        cone = ConeVolume(height, diameter)
        cone.calculate_volume(level_height)


def test_cone_volume_level_returns_error_when_level_is_less_than_zero():
    # Given: A set of cone dimensions and a level height < 0
    diameter = 30
    height = 3.0
    height = 3.0
    level_height = -1.0

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        cone = ConeVolume(height, diameter)
        cone.calculate_volume(level_height)
