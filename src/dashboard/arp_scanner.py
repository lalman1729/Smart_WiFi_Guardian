import subprocess
import re










"""
def scan_router(router_ip):
    devices = []
    # arp-scan or logic here
    return devices

"""

def scan_router(router_ip):
    """
    Runs arp-scan on router subnet
    Returns list of device IPs
    """
    try:
        # Example: arp-scan -l --interface eth0
        result = subprocess.check_output(
            ["arp-scan", "-l"],
            stderr=subprocess.DEVNULL
        ).decode()

        devices = []
        for line in result.splitlines():
            match = re.match(r"(\d+\.\d+\.\d+\.\d+)\s+", line)
            if match:
                ip = match.group(1)
                if ip != router_ip:
                    devices.append(ip)

        return list(set(devices))

    except Exception as e:
        print("ARP scan failed:", e)
        return []


