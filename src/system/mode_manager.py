import subprocess

def enable_monitor_mode():
    print("[*] Switching to Wi-Fi CCTV (Monitor Mode)")
    subprocess.run(["airmon-ng", "start", "wlan0"], stdout=subprocess.DEVNULL)

def disable_monitor_mode():
    subprocess.run(["airmon-ng", "stop", "wlan0mon"], stdout=subprocess.DEVNULL)

def enable_gateway_mode():
    print("[*] Switching to Network Guardian (Gateway Mode)")
    subprocess.run(["ip", "link", "set", "wlan0", "up"])
