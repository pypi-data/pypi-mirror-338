#!/usr/bin/env python3
"""
Command-line interface for Photogrammetry Target Locator
"""

import argparse
import sys
from .main import main

def cli():
    """
    Command-line interface entry point
    """
    parser = argparse.ArgumentParser(description='Calculate target coordinates from camera image using command-line arguments.')

    # Camera Position Arguments
    pos_group = parser.add_argument_group('Camera Position')
    pos_group.add_argument("--lat", type=float, required=True, help="Camera latitude (degrees)")
    pos_group.add_argument("--lon", type=float, required=True, help="Camera longitude (degrees)")
    pos_group.add_argument("--alt", type=float, required=True, help="Camera altitude (meters)")
    pos_group.add_argument("--heading", type=float, required=True, help="Camera heading (0-360 degrees, clockwise from North)")

    # Camera Orientation Arguments
    orient_group = parser.add_argument_group('Camera Orientation')
    orient_group.add_argument("--roll", type=float, required=True, help="Camera roll (degrees)")
    orient_group.add_argument("--pitch", type=float, required=True, help="Camera pitch (degrees)")
    orient_group.add_argument("--yaw", type=float, required=True, help="Camera yaw relative to heading (degrees)")

    # Camera Intrinsics Arguments
    intr_group = parser.add_argument_group('Camera Intrinsics')
    intr_group.add_argument("--hfov", type=float, required=True, help="Horizontal field of view (degrees)")
    intr_group.add_argument("--vfov", type=float, required=True, help="Vertical field of view (degrees)")
    intr_group.add_argument("--width", type=int, required=True, help="Sensor width (pixels)")
    intr_group.add_argument("--height", type=int, required=True, help="Sensor height (pixels)")
    intr_group.add_argument("--px", type=float, help="Principal point X (pixels, default: width/2)")
    intr_group.add_argument("--py", type=float, help="Principal point Y (pixels, default: height/2)")

    # Target Arguments
    target_group = parser.add_argument_group('Target')
    target_group.add_argument("--tx", type=float, required=True, help="Target pixel X coordinate")
    target_group.add_argument("--ty", type=float, required=True, help="Target pixel Y coordinate")

    args = parser.parse_args()

    # Set default principal point if not provided
    if args.px is None:
        args.px = args.width / 2.0
    if args.py is None:
        args.py = args.height / 2.0

    # Run the main function, passing the parsed arguments
    return main(args)

if __name__ == '__main__':
    sys.exit(cli()) 