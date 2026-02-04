from collections import Counter
from dashboard.domain_categories import categorize_domain

DNS_LOG = "logs/dns.log"

def analyze_dns():
    category_count = Counter()
    domain_count = Counter()

    try:
        with open(DNS_LOG) as f:
            for line in f:
                if "query[A]" in line:
                    parts = line.split()
                    domain = parts[-1]

                    category = categorize_domain(domain)
                    category_count[category] += 1
                    domain_count[domain] += 1
    except FileNotFoundError:
        pass

    return category_count, domain_count
