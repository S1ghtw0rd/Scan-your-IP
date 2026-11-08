import argparse
import subprocess
import re
from datetime import datetime
import sys
import shutil
import time

encoding = "cp866" if sys.platform == "win32" else "utf-8"

parser = argparse.ArgumentParser()
parser.add_argument("--ip", required=True, help="Please, write you IP address. Example: 192.168.0.1")
parser.add_argument("--timeout", type=int, default=30000, help="Write time in milliseconds")

args = parser.parse_args()

time_now = datetime.now().strftime("%H:%M:%S")

with open("file.log", "a", encoding=encoding) as str:
    str.write(f"[+] - [{time_now}] Programm is complete start!\n")


def check_nmap():
    if not shutil.which("nmap"):
        with open("file.log", "a", encoding=encoding) as str:
            str.write(f"[-] - [{time_now}] - Nmap is not found\n")
        if sys.platform == "win32":
            print("Nmap is not found - write the command in PowerShell - winget install nmap")
        elif sys.platform.startswith('linux'):
            print("Nmap in not found")
            print("Write in terminal - 'sudo apt install nmap -y' (if your system is Debian-family) or 'sudo dnf install nmap -y' (if your system in RHEL-family)")
        else:
            print(f"Nmap is not found! Please open terminal and write 'sudo port install nmap' ")
        sys.exit(1)

check_nmap()
ip_for_nmap = args.ip

open_port = subprocess.Popen(
    ["nmap", "-sV", "-T4", ip_for_nmap],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding=encoding
)

stdout_port, stderr_port = open_port.communicate()

if open_port.returncode == 0:
    with open("file.log", "a", encoding=encoding) as str:
        str.write(f"[+] - [{time_now}] - Nmap successful scanning your IP - {args.ip}\n")
    time.sleep(5)

    pattern = r"\d+/tcp|udp"
    ports = re.findall(pattern, stdout_port)

    for port in ports:
        with open("file.log", "a", encoding=encoding) as str:
            str.write(f"[+] - [{time_now}] - Successful scan: {ip_for_nmap}, open port - {ports}\n")
            break
    print(f"{args.ip} - open port: {", ".join(ports)}")

else:
    with open("file.log", "a", encoding=encoding) as str:
        str.write(f"[-] - [{time_now}] - Error: {stderr_port}\n")

