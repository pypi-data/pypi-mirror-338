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
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Validate required configuration keys
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
        "target.pixel_coordinates.x",
        "target.pixel_coordinates.y"
    ]
    
    for key_path in required_keys:
        parts = key_path.split('.')
        curr = config
        for part in parts:
            if part not in curr:
                raise KeyError(f"Required configuration key missing: {key_path}")
            curr = curr[part]
    
    # Validate field of view values
    h_fov = config["camera"]["intrinsics"]["field_of_view"]["horizontal_degrees"]
    v_fov = config["camera"]["intrinsics"]["field_of_view"]["vertical_degrees"]
    
    if h_fov <= 0 or h_fov >= 180:
        raise ValueError(f"Horizontal field of view must be between 0 and 180 degrees, got {h_fov}")
    
    if v_fov <= 0 or v_fov >= 180:
        raise ValueError(f"Vertical field of view must be between 0 and 180 degrees, got {v_fov}")
    
    # Validate heading
    heading = config["camera"]["position"]["heading"]
    if heading < 0 or heading >= 360:
        raise ValueError(f"Heading must be between 0 and 360 degrees, got {heading}")
    
    # Add default principal point if not specified (center of image)
    if "principal_point" not in config["camera"]["intrinsics"]:
        image_width = config["camera"]["intrinsics"]["sensor_size"]["width"]
        image_height = config["camera"]["intrinsics"]["sensor_size"]["height"]
        config["camera"]["intrinsics"]["principal_point"] = {
            "x": image_width / 2,
            "y": image_height / 2
        }
    elif "x" not in config["camera"]["intrinsics"]["principal_point"]:
        config["camera"]["intrinsics"]["principal_point"]["x"] = config["camera"]["intrinsics"]["sensor_size"]["width"] / 2
    elif "y" not in config["camera"]["intrinsics"]["principal_point"]:
        config["camera"]["intrinsics"]["principal_point"]["y"] = config["camera"]["intrinsics"]["sensor_size"]["height"] / 2
    
    return config


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
    for part in parts:
        if part not in curr:
            raise KeyError(f"Configuration key not found: {key_path}")
        curr = curr[part]
    return curr 