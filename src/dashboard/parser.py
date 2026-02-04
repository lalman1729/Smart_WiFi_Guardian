
from collections import defaultdict
from .domain_categories import categorize

DNS_LOG = "logs/dns.log"

def parse_dns_log():
    categories = defaultdict(int)
    domains = defaultdict(int)
    devices = defaultdict(lambda: defaultdict(int))
    try:
        with open(DNS_LOG, "r") as f:
            for line in f:
                if "query[A]" in line and "from" in line:
                    parts = line.split()

                         # Extract domain after query[A]
                    try:
                        domain_index = parts.index("query[A]") + 1
                        domain = parts[domain_index]
                    except ValueError:
                        continue

                      # Extract device IP (last word)  
                    device_ip = parts[-1]


                    # TEMP: simulate LAN device instead of localhost
                    if device_ip == "127.0.0.1":
                        device_ip = "10.10.128.10"

                    category = categorize(domain)

                    categories[category] += 1
                    domains[domain] += 1
                    devices[device_ip][domain] += 1
    except FileNotFoundError:
        pass

    return dict(categories), dict(domains), dict(devices)




"""


from collections import Counter, defaultdict
from dashboard.domain_categories import categorize

DNS_LOG = "logs/dns.log"

def parse_dns_log():
    categories = Counter()
    domains = Counter()
    devices = defaultdict(lambda: {
        "categories": Counter(),
        "domains": Counter(),
        "total": 0
    })

    try:
        with open(DNS_LOG) as f:
            for line in f:
                if "query[A]" in line:
                    parts = line.split()
                    domain = parts[-1]
                    device = parts[-3]

                    cat = categorize(domain)

                    categories[cat] += 1
                    domains[domain] += 1

                    devices[device]["categories"][cat] += 1
                    devices[device]["domains"][domain] += 1
                    devices[device]["total"] += 1
    except FileNotFoundError:
        pass

    return categories, domains, devices


"""


"""
from collections import Counter, defaultdict
from .domain_categories import categorize


def parse_dns_log(log_file="logs/dns.log"):
    category_count = Counter()
    domain_count = Counter()
    device_usage = defaultdict(Counter)  # device_ip -> category counter

    try:
        with open(log_file) as f:
            for line in f:
                if "query[A]" in line:
                    parts = line.split()
                    domain = parts[-2]
                    client_ip = parts[-1]

                    category = categorize(domain)

                    category_count[category] += 1
                    domain_count[domain] += 1
                    device_usage[client_ip][category] += 1
    except FileNotFoundError:
        pass

    return category_count, domain_count, device_usage
"""
