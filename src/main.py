from filtering.blocklist_manager import load_blocklists
import time

from scanner.wifi_scanner import start_scanner
from system.mode_manager import enable_monitor_mode, enable_gateway_mode
from network.dns_controller import start_dns

if __name__ == "__main__":

    mode = open("config/mode.conf").read().strip()

    if "MONITOR" in mode:
        enable_monitor_mode()
        start_scanner()

    elif "GATEWAY" in mode:
        enable_gateway_mode()
        start_dns()
        print("[+] Smart Wi-Fi Guardian running in Gateway Mode")
        while True:
            load_blocklists()
            time.sleep(60)

    else:
        print("[!] Unknown mode in config/mode.conf")

