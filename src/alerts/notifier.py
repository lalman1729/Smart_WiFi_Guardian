import subprocess

def desktop_notify(title, message, severity="LOW"):
    urgency = "normal"

    if severity == "HIGH":
        urgency = "critical"
    elif severity == "MEDIUM":
        urgency = "normal"
    else:
        urgency = "low"

    try:
        subprocess.run([
            "notify-send",
            "--urgency", urgency,
            title,
            message
        ])
    except Exception as e:
        print("[!] Notification error:", e)
