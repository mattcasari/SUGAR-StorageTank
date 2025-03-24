from .generic.generic import GenericVolume

def get_volume_obj(config:dict) -> GenericVolume:
    match config['type']:
        case 'box':
            from .box.volume import Volume
            return Volume(config['height'], config['width'], config['depth'])
        
        case 'cylinder':
            from .cylinder.volume import Volume
            return Volume(config['height'], config['diameter'])
        
        case 'cone':
            from .cone.volume import Volume
            return Volume(config['height'], config['diameter'])
        
        case 'horizontal_ellipsoid':
            from .horizontal_half_ellipse.volume import Volume
            return Volume(config['height'], config['width'], config['depth'])
        
        case default:
            raise ValueError(f"Unsupported volume type: {config['type']}")