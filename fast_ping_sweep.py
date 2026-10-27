import socket
import concurrent.futures
import sys

# 1. function scans a one device
def check_host(ip, port=80):
    try:
        # tring make a socket and connect to device
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # بنستنى نص ثانية بس عشان السرعة
        result = s.connect_ex((ip, port))
        s.close()
        
        # if result is 0 the port is openned
        if result == 0:
            return ip
    except:
        pass
    return None

# 2. main function
def main():
    if len(sys.argv) > 1:
        base_ip = sys.argv[1]
    else:
        base_ip = input("Enter base IP (e.g., 192.168.0): ")

    print(f"[*] Starting Fast Ping Sweep on {base_ip}.1 - {base_ip}.254 ...")
    active_hosts = []

    # 3. Scan 100 device on same time
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # make a list of IPs
        ips = [f"{base_ip}.{i}" for i in range(1, 255)]
        
        # run the tool on all IPs
        results = executor.map(check_host, ips)
        
        # Take results
        for result in results:
            if result:
                active_hosts.append(result)
                print(f"[+] Host {result} is UP")

    print(f"\n[*] Scan finished. Found {len(active_hosts)} active hosts.")
    print("[*] Use 'nmap' for more detailed scan on these hosts.")

if __name__ == "__main__":
    main()