🔍 Parker's Port Scanner
Parker's Port Scanner is a lightweight Python-based network utility that scans for open TCP ports on a target host. It's designed as a beginner-friendly project to help users understand how port scanning works and explore basic network reconnaissance techniques.

📌 Features
🎯 Scans ports 1–1024 on a user-specified host (e.g., localhost, domain, or IP address)

🔎 Identifies open TCP ports and attempts to detect the service name (e.g., HTTP, SSH)

📁 Logs all results to a file (Port-Scanner-Results.txt) with timestamps

⏱ Displays start time, end time, and total scan duration

💬 Built-in terminal interface with ASCII banner for style

🚀 Getting Started
Prerequisites
Python 3.x

pyfiglet module for ASCII banner output:

bash
Copy
Edit
pip install pyfiglet
Running the Scanner
bash
Copy
Edit
python3 parker_port_scanner.py
Follow the on-screen prompt to enter a hostname or IP address.

🛠 Example Output
text
Copy
Edit
Parker's Port Scanner

Please enter a host to scan (e.g., localhost or 192.168.1.1): localhost
Scanning started at 12:34:56
Scanning 127.0.0.1...

Port 22 is OPEN (ssh)
Port 80 is OPEN (http)

Scan finished at 12:35:01
Total scan duration: 0:00:05
📚 Use Cases
Networking or cybersecurity practice

Learning about TCP/IP and socket programming

Entry-level recon tool in CTF/home labs

⚠️ Disclaimer
This tool is intended for educational and ethical use only. Always ensure you have permission before scanning any network or system.

