

def in3_to_gallons(volume_in3:float)->float:
    """ Converts cubic inches to gallons

    Args:
        volume_in3 (float): Volume in cubic inches
    Returns:
        float: Volume in gallons
    """
    return volume_in3 / 231


def in_to_cm(length:float)->float:
    """ Converts inches to cm

    Args:
        length (float): inches to convert

    Returns:
        float: cm (from inches)
    """
    
    return length * 2.54

def cm_to_in(length:float)->float:
    """ Converts cm to inches

    Args:
        length (float): cm to convert

    Returns:
        float: inches (from cm)
    """
    return length / 2.54



def find_length_conversion(unit_from:str, unit_to:str)->float:
    """Returns a function that converts a unit to another unit

    Args:
        unit_from (str): Starting unit of length
        unit_to (str): Converted unit of length

    Returns:
        function: function to convert between units
    """
    if unit_from == "in" and unit_to == "cm":
        return 2.54
    elif unit_from == "in" and unit_to == "in":
        return 1
    elif unit_from == "cm" and unit_to == "in":
        return 1/2.54
    elif unit_from == "cm" and unit_to == "cm":
        return 1
    else:
        raise ValueError("Invalid unit conversion")