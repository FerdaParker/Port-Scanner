import socket
import pyfiglet
from datetime import datetime

# Banner
print(pyfiglet.figlet_format("Parker's Port Scanner"))

# Get target host
target = input("Please enter a host to scan (e.g., localhost or 192.168.1.1): ")
try:
    host = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

start_time = datetime.now()
print(f"Scanning started at {start_time.strftime('%H:%M:%S')}")
print(f"Scanning {host}...\n")

with open("Port-Scanner-Results.txt", "w") as file:
    file.write(f"Scan results for {target} ({host})\n")
    file.write(f"Started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 

        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            message = f"Port {port} is OPEN ({service})"
            print(message)
            file.write(message + "\n")

        sock.close()

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\nScan finished at {end_time.strftime('%H:%M:%S')}")
    print(f"Total scan duration: {duration}")
    file.write(f"\nScan finished at {end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Total scan duration: {duration}\n")
