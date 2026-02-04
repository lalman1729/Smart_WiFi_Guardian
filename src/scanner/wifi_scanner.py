from scapy.all import sniff
from scapy.layers.dot11 import Dot11
from detection.evil_twin import detect_evil_twin
from detection.deauth_attack import detect_deauth_attack

def handle_packet(packet):
    if packet.haslayer(Dot11):
        detect_evil_twin(packet)
        detect_deauth_attack(packet)

def start_scanner(interface="wlan0mon"):
    print(f"[+] Smart Wi-Fi Guardian active on {interface}")
    sniff(iface=interface, prn=handle_packet, store=False)









"""

from scapy.all import sniff
from scapy.layers.dot11 import Dot11
from detection.evil_twin import detect_evil_twin

def handle_packet(packet):
    if packet.haslayer(Dot11):
        detect_evil_twin(packet)

def start_scanner(interface="wlan0mon"):
    print(f"[+] Smart Wi-Fi Guardian scanning on {interface}")
    sniff(iface=interface, prn=handle_packet, store=False)

"""


"""
from scapy.all import sniff
from scapy.layers.dot11 import Dot11
import datetime

def handle_packet(packet):
    if packet.haslayer(Dot11):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src = packet.addr2
        dst = packet.addr1
        bssid = packet.addr3
        frame_type = packet.type
        frame_subtype = packet.subtype

        print(f"[{timestamp}] SRC:{src} DST:{dst} BSSID:{bssid} TYPE:{frame_type}:{frame_subtype}")

def start_scanner(interface="wlan0mon"):
    print(f"[+] Starting Wi-Fi packet scanner on {interface}")
    sniff(iface=interface, prn=handle_packet, store=False)
"""
