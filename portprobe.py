#!/usr/bin/env python3
import argparse
import socket
from banner import printBanner
from scanner import scanPort, scanPorts, currentTimestamp
from help import helpMessage

def main():
    """
    Main function to parse arguments and initiate the port scanning.
    """
    # Print the banner
    printBanner()
    
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Port Probe - A simple port scanner',
        add_help=False
    )
    
    # Add arguments to the parser
    parser.add_argument('-t', '--target', type=str, help='IP address or hostname of the target to scan')
    parser.add_argument('-p', '--port', type=int, help='Single port number to scan')
    parser.add_argument('-sp', '--start-port', type=int, help='Starting port number (used if -p is not specified)')
    parser.add_argument('-ep', '--end-port', type=int, help='Ending port number (used if -p is not specified)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode to show closed ports')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    
    # Parse the arguments
    args = parser.parse_args()

    # If help is requested, print the help message
    if args.help or not any(vars(args).values()):
        print(helpMessage())
        return

    # Resolve hostname to IP address if necessary
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {args.target}")
        return
    
    # Perform the scan
    if args.port:
        if args.verbose:
            print(f"Scanning {args.target} ({target_ip}) on port {args.port}")
        scanPort(target_ip, args.port, args.verbose)
    else:
        # If no single port is specified, use the start and end port range
        if not args.start_port:
            args.start_port = 1  # Default starting port
        if not args.end_port:
            args.end_port = 1024  # Default ending port
        if args.verbose:
            print(f"Scanning {args.target} ({target_ip}) from port {args.start_port} to {args.end_port}")
        scanPorts(target_ip, args.start_port, args.end_port, args.verbose)
    
    # Print the timestamp at which the scan is completed
    print("\nScan completed at:", currentTimestamp())



if __name__ == "__main__":
    main()
