from scapy.layers.dot11 import Dot11, Dot11Beacon
from logger.event_logger import log_event
from detection.risk_engine import update_risk

# Known SSID -> BSSID mapping
known_networks = {}

def detect_evil_twin(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Beacon].network_stats().get("ssid")
        bssid = packet[Dot11].addr2

        if ssid:
            # Learn legitimate network
            if ssid not in known_networks:
                known_networks[ssid] = bssid
                log_event(
                    event_type="NETWORK_LEARNED",
                    details={
                        "ssid": ssid,
                        "bssid": bssid
                    },
                    severity="LOW"
                )

            # Evil Twin detected
            elif known_networks[ssid] != bssid:
                log_event(
                    event_type="EVIL_TWIN_DETECTED",
                    details={
                        "ssid": ssid,
                        "legitimate_bssid": known_networks[ssid],
                        "rogue_bssid": bssid
                    },
                    severity="HIGH"
                )

                # Update risk score
                update_risk(
                    event_type="EVIL_TWIN_DETECTED",
                    details={"ssid": ssid}
                )











"""
from scapy.layers.dot11 import Dot11, Dot11Beacon
import datetime

# Known SSID -> BSSID mapping
known_networks = {}

def detect_evil_twin(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Beacon].network_stats().get("ssid")
        bssid = packet[Dot11].addr2

        if ssid:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # First time seeing this SSID
            if ssid not in known_networks:
                known_networks[ssid] = bssid
                print(f"[INFO] [{timestamp}] Learned network: {ssid} ({bssid})")

            # Same SSID, different BSSID = Evil Twin
            elif known_networks[ssid] != bssid:
                print(f"[ALERT] [{timestamp}] EVIL TWIN DETECTED!")
                print(f"        SSID : {ssid}")
                print(f"        Legit: {known_networks[ssid]}")
                print(f"        Rogue: {bssid}")



"""
