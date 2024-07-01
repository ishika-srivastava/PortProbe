def helpMessage():
    return"""
Port Probe - A simple port scanner.
Usage: portprobe -t <TARGET> -p <PORT> | -sp <START_PORT> -ep <END_PORT>

arguments:
-h, --help: show the help message and exit
-t <TARGET>, --target: TARGET IP address or hostname of the target to scan
-p <PORT>, --port <PORT>: Single port number to scan
-sp <START_PORT>, --start-port <START_PORT>: Starting port number (used if -p is not specified)
-ep <END_PORT>, --end-port <END_PORT>: Ending port number (used if -p is not specified)
-v, --verbose: Enable verbose mode to show closed ports
"""
