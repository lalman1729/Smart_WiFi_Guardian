import os
from control.time_rules import get_active_blocks

BLOCKLIST_DIR = "config/blocklists"
DNS_BLOCK_FILE = "config/dns/blocked_domains.conf"

def load_blocklists():
    active_categories = get_active_blocks()
    blocked = []

    if not active_categories:
        print("[*] No active time blocks")
    else:
        print("[*] Active blocks:", active_categories)

    for file in os.listdir(BLOCKLIST_DIR):
        category = file.replace(".txt", "")

        if category not in active_categories:
            continue

        path = os.path.join(BLOCKLIST_DIR, file)
        with open(path) as f:
            for line in f:
                domain = line.strip()
                if domain and not domain.startswith("#"):
                    blocked.append(domain)

    with open(DNS_BLOCK_FILE, "w") as f:
        for domain in blocked:
            f.write(f"address=/{domain}/0.0.0.0\n")

    print(f"[+] Applied {len(blocked)} time-based blocks")

if __name__ == "__main__":
    load_blocklists()

