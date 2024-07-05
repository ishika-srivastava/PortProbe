# scanner.py

import socket
from datetime import datetime
import threading
from queue import Queue

# Common ports and services
COMMON_PORTS = {
    20: 'FTP Data',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3389: 'RDP',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    5900: 'VNC',
    6379: 'Redis',
    8080: 'HTTP Proxy',
}

def serviceName(port):
    """
    Get the service name for a given port number.
    """
    return COMMON_PORTS.get(port, 'Unknown Service')

def scanPort(ip, port, verbose=False):
    """
    Scan a single port on the target IP address.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service_name = serviceName(port)
            print(f"Port {port}: OPEN ({service_name})")
        else:
            if verbose:
                print(f"Port {port}: CLOSED")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port} : {e}")


def scanPorts(ip, start_port, end_port, verbose=False, thread_count=100):
    """
    Scan a range of ports on the target IP address using multi-threading.
    """
    def worker(port_queue):
        while not port_queue.empty():
            port = port_queue.get()
            scanPort(ip, port, verbose)
            port_queue.task_done()

    port_queue = Queue()
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=worker, args=(port_queue,))
        thread.start()
        threads.append(thread)

    port_queue.join()

    for thread in threads:
        thread.join()



def currentTimestamp():
    """
    Get the current timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
