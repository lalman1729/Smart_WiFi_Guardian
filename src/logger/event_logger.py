

import datetime
import json
import os
from alerts.notifier import desktop_notify

LOG_FILE = "logs/alerts.log"

def log_event(event_type, details, severity="MEDIUM"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = {
        "time": timestamp,
        "type": event_type,
        "severity": severity,
        "details": details
    }

    # Ensure log directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    # Console output
    print(f"[{severity}] {event_type} @ {timestamp}")

    # Desktop notification (only for important events)
    if severity in ["HIGH", "CRITICAL"]:
        desktop_notify(
            title="🛡 Smart Wi-Fi Guardian Alert",
            message=f"{event_type}\n{details}",
            severity=severity
        )










"""
import datetime
import json
import os

LOG_FILE = "logs/alerts.log"

def log_event(event_type, details, severity="MEDIUM"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = {
        "time": timestamp,
        "type": event_type,
        "severity": severity,
        "details": details
    }

    # Ensure log directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

    # Console alert
    print(f"[{severity}] {event_type} @ {timestamp}")
"""
