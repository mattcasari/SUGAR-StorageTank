import pytest
from src.storage_tank import StorageTank
from src.utils.math.volumes.cone.volume import Volume as ConeVolume
from src.utils.math.volumes.cylinder.volume import Volume as CylinderVolume


def test_storage_tank_basic_setup_cone_bottom_and_cylinder_top():
    # Given: a basic setup
    get_distance = lambda: 10  # Mock distance sensor function
    cone_height = 19.0
    cone_diameter = 77
    cylinder_height = 48.0
    cylinder_diameter = cone_diameter
    upper_tank = CylinderVolume(cylinder_height, cylinder_diameter)  # Mock upper tank volume
    lower_tank = ConeVolume(cone_height, cone_diameter)  # Mock lower tank volume
    mounted_distance = 0  # Distance sensor is mounted above top of tank

    # When: a StorageTank object is created
    tank = StorageTank(
        get_distance=get_distance,
        upper_tank=upper_tank,
        lower_tank=lower_tank,
        mounted_distance=mounted_distance,
    )  # Mock

    # Then: the tank object should be initialized correctly
    expected_total_max_height = 67.0
    expected_total_max_volume = 223518 + 29492

    assert expected_total_max_height == tank._max_height
    assert expected_total_max_volume == pytest.approx(tank._max_volume, 1e0)


def test_storage_tank_cone_bottom_and_cylinder_top_calc_low_height():
    # Given: a basic setup with a level that is only partially filling the lower volume
    get_distance = lambda: 57.0  # Mock distance sensor function
    cone_height = 19.0
    cone_diameter = 77
    cylinder_height = 48.0
    cylinder_diameter = cone_diameter
    upper_tank = CylinderVolume(cylinder_height, cylinder_diameter)  # Mock upper tank volume
    lower_tank = ConeVolume(cone_height, cone_diameter)  # Mock lower tank volume
    mounted_distance = 0  # Distance sensor is mounted above top of tank

    # When: a StorageTank object is created
    tank = StorageTank(
        get_distance=get_distance,
        upper_tank=upper_tank,
        lower_tank=lower_tank,
        mounted_distance=mounted_distance,
    )  # Mock

    # Then: the tank object should be initialized correctly
    expected_volume = 4300
    expected_depth = 10.0

    (volume, depth) = tank.read_tank()
    print(f"{volume=}")
    assert volume == pytest.approx(expected_volume, 1e0)
    assert depth == pytest.approx(expected_depth, 1e0)


def test_storage_tank_cone_bottom_and_cylinder_top_calc_high_height():
    # Given: a basic setup with a level that is only partially filling the upper volume and all the lower volume
    get_distance = lambda: 10.0  # Mock distance sensor function
    cone_height = 19.0
    cone_diameter = 77
    cylinder_height = 48.0
    cylinder_diameter = cone_diameter
    upper_tank = CylinderVolume(cylinder_height, cylinder_diameter)  # Mock upper tank volume
    lower_tank = ConeVolume(cone_height, cone_diameter)  # Mock lower tank volume
    mounted_distance = 0  # Distance sensor is mounted above top of tank

    # When: a StorageTank object is created
    tank = StorageTank(
        get_distance=get_distance,
        upper_tank=upper_tank,
        lower_tank=lower_tank,
        mounted_distance=mounted_distance,
    )  # Mock

    # Then: the tank object should be initialized correctly
    expected_volume = (176952 + 29492) / 231
    expected_depth = 57.0

    (volume, depth) = tank.read_tank()
    assert volume == pytest.approx(expected_volume, 1e-2)
    assert depth == pytest.approx(expected_depth)


def test_storage_tank_cone_bottom_and_cylinder_top_level_below_zero():
    # Given: a basic setup with a level that is reporting a level below zero
    get_distance = lambda: 67.1  # Would be depth of -0.1
    cone_height = 19.0
    cone_diameter = 77
    cylinder_height = 48.0
    cylinder_diameter = cone_diameter
    upper_tank = CylinderVolume(cylinder_height, cylinder_diameter)  # Mock upper tank volume
    lower_tank = ConeVolume(cone_height, cone_diameter)  # Mock lower tank volume
    mounted_distance = 0  # Distance sensor is mounted above top of tank

    # When: a StorageTank object is created
    tank = StorageTank(
        get_distance=get_distance,
        upper_tank=upper_tank,
        lower_tank=lower_tank,
        mounted_distance=mounted_distance,
    )  # Mock

    # Then: the tank object should return zero
    expected_volume = 0
    expected_depth = 0

    (volume, depth) = tank.read_tank()
    assert volume == pytest.approx(expected_volume, 1e-2)
    assert depth == pytest.approx(expected_depth)


def test_storage_tank_cone_bottom_and_cylinder_top_level_above_max():
    # Given: a basic setup with a level that is reporting a level below zero
    get_distance = lambda: -0.1  # Would be a depth of 67.1
    cone_height = 19.0
    cone_diameter = 77
    cylinder_height = 48.0
    cylinder_diameter = cone_diameter
    upper_tank = CylinderVolume(cylinder_height, cylinder_diameter)  # Mock upper tank volume
    lower_tank = ConeVolume(cone_height, cone_diameter)  # Mock lower tank volume
    mounted_distance = 0  # Distance sensor is mounted above top of tank

    # When: a StorageTank object is created
    tank = StorageTank(
        get_distance=get_distance,
        upper_tank=upper_tank,
        lower_tank=lower_tank,
        mounted_distance=mounted_distance,
    )  # Mock

    # Then: the tank object should return zero
    expected_volume = (tank._lower_tank.MAX_VOLUME + tank._upper_tank.MAX_VOLUME) / 231
    expected_depth = 67.0

    (volume, depth) = tank.read_tank()
    assert volume == pytest.approx(expected_volume, 1e-2)
    assert depth == pytest.approx(expected_depth)
