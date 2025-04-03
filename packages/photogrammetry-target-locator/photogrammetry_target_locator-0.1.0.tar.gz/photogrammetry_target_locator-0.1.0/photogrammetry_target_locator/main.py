import json
import sys
import os
from .config import load_config
from .photogrammetry import calculate_target_coordinates


def main():
    """
    Main function to run the photogrammetry calculations.
    Loads config, performs calculation, and prints results.
    """
    # Check if a config file path was provided as a command-line argument
    config_path = "config.json"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    
    try:
        # Load configuration
        print(f"Loading configuration from {config_path}...")
        config = load_config(config_path)
        
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
            
            # Also fix the altitude in the result json for consistency
            result["target"]["altitude"] = altitude
        else:
            print(f"Error: {result['error']}")
            return 1
        
        # Optionally save results to a file
        output_file = os.path.splitext(config_path)[0] + "_result.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\nResults saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 