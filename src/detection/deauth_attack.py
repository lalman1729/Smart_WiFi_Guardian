from scapy.layers.dot11 import Dot11Deauth, Dot11
import time
from logger.event_logger import log_event
from detection.risk_engine import update_risk

# Store deauth counts per source
deauth_tracker = {}

# Thresholds
DEAUTH_LIMIT = 20     # packets
TIME_WINDOW = 5       # seconds

def detect_deauth_attack(packet):
    if packet.haslayer(Dot11Deauth):
        src = packet[Dot11].addr2
        now = time.time()

        if src not in deauth_tracker:
            deauth_tracker[src] = []

        # Add timestamp
        deauth_tracker[src].append(now)

        # Remove old timestamps
        deauth_tracker[src] = [
            t for t in deauth_tracker[src]
            if now - t <= TIME_WINDOW
        ]

        # 🚨 Deauth flood detected
        if len(deauth_tracker[src]) >= DEAUTH_LIMIT:
            # 1️⃣ Log the event
            log_event(
                event_type="DEAUTH_FLOOD_DETECTED",
                details={
                    "source_mac": src,
                    "count": len(deauth_tracker[src]),
                    "time_window_seconds": TIME_WINDOW
                },
                severity="HIGH"
            )

            # 2️⃣ UPDATE RISK SCORE (THIS IS THE PART YOU ASKED ABOUT)
            update_risk(
                event_type="DEAUTH_FLOOD_DETECTED",
                details={"source_mac": src}
            )

            # 3️⃣ Reset counter to avoid repeated alerts
            deauth_tracker[src].clear()












"""
from scapy.layers.dot11 import Dot11Deauth, Dot11
import time
from logger.event_logger import log_event

# Store deauth counts per source
deauth_tracker = {}

# Thresholds (can later move to config)
DEAUTH_LIMIT = 20        # packets
TIME_WINDOW = 5          # seconds

def detect_deauth_attack(packet):
    if packet.haslayer(Dot11Deauth):
        src = packet[Dot11].addr2
        now = time.time()

        if src not in deauth_tracker:
            deauth_tracker[src] = []

        # Add timestamp
        deauth_tracker[src].append(now)

        # Remove old timestamps
        deauth_tracker[src] = [
            t for t in deauth_tracker[src] if now - t <= TIME_WINDOW
        ]

        # Detect flood
        if len(deauth_tracker[src]) >= DEAUTH_LIMIT:
            log_event(
                event_type="DEAUTH_FLOOD_DETECTED",
                details={
                    "source_mac": src,
                    "count": len(deauth_tracker[src]),

                    "time_window_seconds": TIME_WINDOW

                },


                severity="HIGH"
            )





            # Reset to avoid repeated alerts
            deauth_tracker[src].clear()
"""
