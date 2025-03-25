from .generic.generic import GenericVolume


def get_volume_obj(config: dict) -> GenericVolume:
    print(config)
    if config["type"] == "box":
        from .box.volume import Volume

        return Volume(config["height"], config["width"], config["depth"])

    elif config["type"] == "cylinder":
        from .cylinder.volume import Volume

        return Volume(config["height"], config["diameter"])

    elif config["type"] == "cone":
        from .cone.volume import Volume

        return Volume(config["height"], config["diameter"])

    elif config["type"] == "horizontal_ellipsoid":
        from .horizontal_half_ellipse.volume import Volume

        return Volume(config["height"], config["width"], config["depth"])

    else:
        raise ValueError(f"Unsupported volume type: {config['type']}")
