import socket
import sys

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # بنستنى نص ثانية بس
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"[+] البورت {port} مفتوح")
    s.close()

if len(sys.argv) > 1:
    target_ip = sys.argv[1]

else:

    target_ip = "127.0.0.1"

print(f"start scan {target_ip} ...")

# بنلف على أول 10 بورتات مشهورة
for p in [21, 22, 7547, 1900, 53, 8080]:
    scan_port(target_ip, p)
    print("Finished scan")

