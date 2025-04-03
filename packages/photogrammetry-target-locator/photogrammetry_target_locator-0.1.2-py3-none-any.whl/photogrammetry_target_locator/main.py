import json
import sys
import os
import argparse
from .config import validate_config_values
from .photogrammetry import calculate_target_coordinates


def main(args: argparse.Namespace) -> int:
    """
    Main function to run the photogrammetry calculations.
    Takes parsed command-line arguments, performs calculation, and prints results.
    
    Args:
        args: Parsed command-line arguments from argparse
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Build the config dictionary from arguments
        config = {
            "camera": {
                "position": {
                    "latitude": args.lat,
                    "longitude": args.lon,
                    "altitude": args.alt,
                    "heading": args.heading
                },
                "orientation": {
                    "roll": args.roll,
                    "pitch": args.pitch,
                    "yaw": args.yaw
                },
                "intrinsics": {
                    "field_of_view": {
                        "horizontal_degrees": args.hfov,
                        "vertical_degrees": args.vfov
                    },
                    "sensor_size": {
                        "width": args.width,
                        "height": args.height
                    },
                    "principal_point": {
                        "x": args.px,
                        "y": args.py
                    }
                }
            },
            "target": {
                "pixel_coordinates": {
                    "x": args.tx,
                    "y": args.ty
                }
            }
        }
        
        # Validate the constructed config values
        validate_config_values(config)
        
        # Calculate target coordinates
        print("Calculating target coordinates...")
        result = calculate_target_coordinates(config)
        
        # Print results
        if result["success"]:
            target = result["target"]
            
            # Round the altitude to 2 decimal places and ensure small values are shown as 0.00
            altitude = target["altitude"]
            if abs(altitude) < 0.01:
                altitude = 0.0
            
            # Check if there were any warnings during calculation
            if "warning" in result:
                print(f"\nWarning: {result['warning']}")
                
            print("\nTarget coordinates:")
            print(f"  Latitude:  {target['latitude']:.8f} degrees")
            print(f"  Longitude: {target['longitude']:.8f} degrees")
            print(f"  Altitude:  {altitude:.2f} meters")
            
            # Output results as JSON to stdout
            # Prepare result dictionary for JSON output (ensuring altitude fix)
            json_result = result.copy()
            json_result["target"]["altitude"] = altitude
            print("\nJSON Result:")
            print(json.dumps(json_result, indent=2))
        else:
            print(f"Error: {result['error']}")
            return 1
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Photogrammetry Target Locator")
    parser.add_argument("--lat", type=float, required=True, help="Latitude of the camera")
    parser.add_argument("--lon", type=float, required=True, help="Longitude of the camera")
    parser.add_argument("--alt", type=float, required=True, help="Altitude of the camera")
    parser.add_argument("--heading", type=float, required=True, help="Heading of the camera")
    parser.add_argument("--roll", type=float, required=True, help="Roll angle of the camera")
    parser.add_argument("--pitch", type=float, required=True, help="Pitch angle of the camera")
    parser.add_argument("--yaw", type=float, required=True, help="Yaw angle of the camera")
    parser.add_argument("--hfov", type=float, required=True, help="Horizontal field of view of the camera")
    parser.add_argument("--vfov", type=float, required=True, help="Vertical field of view of the camera")
    parser.add_argument("--width", type=int, required=True, help="Width of the camera sensor")
    parser.add_argument("--height", type=int, required=True, help="Height of the camera sensor")
    parser.add_argument("--px", type=float, required=True, help="X coordinate of the camera's principal point")
    parser.add_argument("--py", type=float, required=True, help="Y coordinate of the camera's principal point")
    parser.add_argument("--tx", type=float, required=True, help="X coordinate of the target in the image")
    parser.add_argument("--ty", type=float, required=True, help="Y coordinate of the target in the image")
    args = parser.parse_args()
    sys.exit(main(args)) 