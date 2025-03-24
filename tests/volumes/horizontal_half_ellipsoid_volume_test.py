import pytest
from src.utils.math.volumes.horizontal_half_ellipse.volume import Volume as HHEVolume


def test_half_horizontal_ellipsoid_volume_for_known_valid_volume():
    # Given: a set of half_horizontal_ellipsoid dimensions with known volume

    height = 3.0
    width = 5.0
    depth = 10.0
    expected_volume = 117.8

    # When: The half_horizontal_ellipsoid Volume object is created
    half_horizontal_ellipsoid = HHEVolume(height, width, depth)

    # Then: The calculated total volume is correct
    assert half_horizontal_ellipsoid.MAX_VOLUME == pytest.approx(expected_volume, abs=1e-2)


def test_half_horizontal_ellipsoid_volume_level_for_known_level_volume():
    # Given: a set of half_horizontal_ellipsoid dimensions and a known volume level
    height = 3.0
    width = 5.0
    depth = 10.0
    level_height = 2.0
    expected_volume_level = 68.8

    # When: The half_horizontal_ellipsoid Volume object is created
    half_horizontal_ellipsoid = HHEVolume(height, width, depth)

    # Then: The calculated level volume is correct
    assert half_horizontal_ellipsoid.calculate_volume(level_height) == pytest.approx(
        expected_volume_level, abs=1e-1
    )


def test_half_horizontal_ellipsoid_volume_level_returns_error_when_level_is_above_max():
    # Given: A set of half_horizontal_ellipsoid dimensions and a level height > max height
    height = 3.0
    width = 5.0
    depth = 10.0
    level_height = 3.01

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        half_horizontal_ellipsoid = HHEVolume(height, width, depth)
        half_horizontal_ellipsoid.calculate_volume(level_height)


def test_half_horizontal_ellipsoid_volume_level_returns_error_when_level_is_less_than_zero():
    # Given: A set of half_horizontal_ellipsoid dimensions and a level height < 0
    height = 3.0
    width = 5.0
    depth = 10.0
    level_height = -1.0

    # When: calculated_volume method is called
    # Then: A ValueError is raised
    with pytest.raises(ValueError):
        half_horizontal_ellipsoid = HHEVolume(height, width, depth)
        half_horizontal_ellipsoid.calculate_volume(level_height)
