def calculate_risk(domains):
    score = 0

    for domain, hits in domains.items():
        d = domain.lower()

        if any(x in d for x in ["malware", "phishing", "hack"]):
            score += 40
        elif any(x in d for x in ["facebook", "instagram", "twitter"]
def calculate_risk(domains):
    score = 0

    for domain, hits in domains.items():
        d = domain.lower()

        if any(x in d for x in ["malware", "phishing", "hack"]):
            score += 40
        elif any(x in d for x in ["facebook", "instagram", "twitter"]

