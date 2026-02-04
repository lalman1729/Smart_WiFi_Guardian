# Domain → Category mapping

CATEGORIES = {
    "education": [
        "wikipedia.org",
        "khanacademy.org",
        "coursera.org"
    ],
    "entertainment": [
        "youtube.com",
        "netflix.com",
        "primevideo.com"
    ],
    "social": [
        "facebook.com",
        "instagram.com",
        "twitter.com"
    ],
    "gaming": [
        "roblox.com",
        "steamcommunity.com",
        "epicgames.com"
    ]
}

def categorize(domain):
    domain = domain.lower()
    for category, domains in CATEGORIES.items():
        for d in domains:
            if d in domain:
                return category
    return "other"

