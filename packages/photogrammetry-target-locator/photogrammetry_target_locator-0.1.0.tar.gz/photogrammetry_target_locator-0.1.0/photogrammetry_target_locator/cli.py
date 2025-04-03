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
    parser = argparse.ArgumentParser(description='Calculate target coordinates from camera image')
    parser.add_argument('config_file', nargs='?', default='config.json',
                        help='Path to configuration file (default: config.json)')
    
    args = parser.parse_args()
    
    # Pass the config file path to main
    sys.argv = [sys.argv[0]]
    if args.config_file != 'config.json':
        sys.argv.append(args.config_file)
    
    # Run the main function
    return main()

if __name__ == '__main__':
    sys.exit(cli()) 