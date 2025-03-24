import pytest
from src.utils.math.volumes.box.volume import Volume as BoxVolume


def test_box_volume_for_known_valid_volume():
    # Given: a set of box dimensions with known volume
    depth = 10.0
    width = 5.0
    height = 3.0
    expected_volume = 150.0

    # When: The box Volume object is created
    box = BoxVolume(height, width, depth)

    # Then: The calculated total volume is correct
    assert box.MAX_VOLUME == expected_volume


def test_box_volume_level_for_known_level_volume():
    # Given: a set of box dimensions and a known volume level
    depth = 10.0
    width = 5.0
    height = 3.0
    level_height = 2.0
    expected_volume_level = 100.0

    # When: The box Volume object is created
    box = BoxVolume(height, width, depth)

    # Then: The calculated volume level is correct
    assert box.calculate_volume(level_height) == expected_volume_level


def test_box_volume_level_returns_error_when_level_is_above_max():
    # Given: A set of box dimensions and a level height > max height
    depth = 10.0
    width = 5.0
    height = 3.0
    level_height = 3.01

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        box = BoxVolume(height, width, depth)
        box.calculate_volume(level_height)


def test_box_volume_level_returns_error_when_level_is_less_than_zero():
    # Given: A set of box dimensions and a level height < 0
    depth = 10.0
    width = 5.0
    height = 3.0
    level_height = -1.0

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        box = BoxVolume(height, width, depth)
        box.calculate_volume(level_height)
