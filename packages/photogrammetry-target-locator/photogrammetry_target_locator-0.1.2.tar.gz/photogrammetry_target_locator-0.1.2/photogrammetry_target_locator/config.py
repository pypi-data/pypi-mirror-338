import json
import os
from typing import Dict, Any


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from a JSON file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary containing the configuration
        
    Raises:
        FileNotFoundError: If the configuration file does not exist
        json.JSONDecodeError: If the configuration file is not valid JSON
        KeyError: If a required key is missing
        ValueError: If a value is out of the expected range
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
        
    # Validate the loaded configuration
    validate_config_values(config)
    
    return config


def validate_config_values(config: Dict[str, Any]):
    """
    Validate the structure and values of the configuration dictionary.
    
    Args:
        config: Configuration dictionary
        
    Raises:
        KeyError: If a required key is missing
        ValueError: If a value is out of the expected range
    """
    required_keys = [
        "camera.position.latitude",
        "camera.position.longitude",
        "camera.position.altitude",
        "camera.position.heading",
        "camera.orientation.roll",
        "camera.orientation.pitch",
        "camera.orientation.yaw",
        "camera.intrinsics.field_of_view.horizontal_degrees",
        "camera.intrinsics.field_of_view.vertical_degrees",
        "camera.intrinsics.sensor_size.width",
        "camera.intrinsics.sensor_size.height",
        "camera.intrinsics.principal_point.x",
        "camera.intrinsics.principal_point.y",
        "target.pixel_coordinates.x",
        "target.pixel_coordinates.y"
    ]
    
    # Check required keys
    for key_path in required_keys:
        get_nested_value(config, key_path) # This will raise KeyError if missing
        
    # Validate field of view values
    h_fov = get_nested_value(config, "camera.intrinsics.field_of_view.horizontal_degrees")
    v_fov = get_nested_value(config, "camera.intrinsics.field_of_view.vertical_degrees")
    
    if not (0 < h_fov < 180):
        raise ValueError(f"Horizontal field of view must be between 0 and 180 degrees, got {h_fov}")
    
    if not (0 < v_fov < 180):
        raise ValueError(f"Vertical field of view must be between 0 and 180 degrees, got {v_fov}")
    
    # Validate heading
    heading = get_nested_value(config, "camera.position.heading")
    if not (0 <= heading < 360):
        raise ValueError(f"Heading must be between 0 and 360 degrees, got {heading}")
    
    # Validate sensor size
    width = get_nested_value(config, "camera.intrinsics.sensor_size.width")
    height = get_nested_value(config, "camera.intrinsics.sensor_size.height")
    if width <= 0 or height <= 0:
        raise ValueError(f"Sensor width and height must be positive, got {width}x{height}")

    # Validate principal point (relative to sensor size)
    px = get_nested_value(config, "camera.intrinsics.principal_point.x")
    py = get_nested_value(config, "camera.intrinsics.principal_point.y")
    if not (0 <= px < width) or not (0 <= py < height):
         print(f"Warning: Principal point ({px}, {py}) is outside sensor dimensions ({width}x{height}). This might be valid for specific camera models but is unusual.")

    # Validate target pixel coordinates (relative to sensor size)
    tx = get_nested_value(config, "target.pixel_coordinates.x")
    ty = get_nested_value(config, "target.pixel_coordinates.y")
    if not (0 <= tx < width) or not (0 <= ty < height):
        raise ValueError(f"Target pixel coordinates ({tx}, {ty}) are outside sensor dimensions ({width}x{height})")


def get_nested_value(config: Dict[str, Any], key_path: str) -> Any:
    """
    Get a nested value from the configuration dictionary.
    
    Args:
        config: Configuration dictionary
        key_path: Dot-separated path to the key
        
    Returns:
        The value at the specified path
        
    Raises:
        KeyError: If the key does not exist
    """
    parts = key_path.split('.')
    curr = config
    try:
        for part in parts:
            curr = curr[part]
        return curr
    except (KeyError, TypeError) as e:
        raise KeyError(f"Configuration key not found or invalid structure: {key_path}") from e 