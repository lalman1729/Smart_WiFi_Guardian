import subprocess
import time
import os

DNS_CONF = "config/dns/guardian_dns.conf"

def start_dns():
    print("[*] Starting Guardian DNS service...")

    # Kill any existing dnsmasq (clean start)
    subprocess.run(["pkill", "dnsmasq"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(1)

    try:
        subprocess.Popen(
            ["dnsmasq", "--conf-file=" + os.path.abspath(DNS_CONF)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("[+] DNS service running on port 5353")
    except Exception as e:
        print("[!] Failed to start DNS:", e)


def stop_dns():
    print("[*] Stopping DNS service...")
    subprocess.run(["pkill", "dnsmasq"], stdout=subprocess.DEVNULL)
