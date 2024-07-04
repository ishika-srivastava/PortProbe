# PortProbe

**PortProbe** is a simple and effective port scanner similar to `nmap`. It allows you to scan ports on a target IP address or hostname to identify open and closed ports, the services running on them, and the protocols used. This tool also supports multi-threading to speed up the scanning process.

## Features

- Identify open ports on a target
- Display the services running on open ports
- Support for multi-threading to speed up scans
- Interactive mode for real-time scanning

## Installation

To install and use **Port Probe**, follow these steps:

1. Clone the repository:
   ```
   $ git clone https://github.com/ishika-srivastava/PortProbe.git
   ```
2. Navigate to the project directory:
   ```
   $ cd PortProbe
   ```
3. Install the required dependencies:
   ```
   $ pip install -r requirements.txt
   ```
   
## Usage
  ```
  $ python portprobe.py --help
   ______          _    ______          _
   | ___ \        | |   | ___ \        | |
   | |_/ /__  _ __| |_  | |_/ / __ ___ | |__   ___
   |  __/ _ \| '__| __| |  __/ '__/ _ \| '_ \ / _ \
   | | | (_) | |  | |_  | |  | | | (_) | |_) |  __/
   \_|  \___/|_|   \__| \_|  |_|  \___/|_.__/ \___|



  -------------------------------------------------
  Port Probe - A Port Scanner
  Created by: Ishika Srivastava
  GitHub : https://github.com/ishika-srivastava/PortProbe
  Version: 1.0
  License: MIT
  (c) 2024 Ishika Srivastava. All rights reserved.
  -------------------------------------------------


  Port Probe - A simple port scanner.
  Usage: portprobe -t <TARGET> -p <PORT> | -sp <START_PORT> -ep <END_PORT>

  arguments:
  -h, --help: show the help message and exit
  -t <TARGET>, --target: TARGET IP address or hostname of the target to scan
  -p <PORT>, --port <PORT>: Single port number to scan
  -sp <START_PORT>, --start-port <START_PORT>: Starting port number (used if -p is not specified)
  -ep <END_PORT>, --end-port <END_PORT>: Ending port number (used if -p is not specified)
  -v, --verbose: Enable verbose mode to show closed ports
  ```
- scan a specific port
  ```
  $ portprobe -t www.google.com -p 80
  ```
- scan a range of ports
  ```
  $ portprobe -t www.google.com -sp 1 -ep 1024
  ```

##Contributing
To contribute to this project, please fork the repository and create a pull request with your changes.

##License
This project is licensed under the MIT License - see the LICENSE file for details.

##Contact
If you have any questions or suggestions, please contact me at ishika.srivastava029@gmail.com
