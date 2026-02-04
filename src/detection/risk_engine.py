from logger.event_logger import log_event

# Risk weights (can later move to config)
RISK_WEIGHTS = {
    "EVIL_TWIN_DETECTED": 60,
    "DEAUTH_FLOOD_DETECTED": 30,
}

risk_state = {
    "score": 0,
    "events": []
}

def update_risk(event_type, details):
    weight = RISK_WEIGHTS.get(event_type, 0)
    risk_state["score"] += weight
    risk_state["events"].append(event_type)

    # Cap score
    if risk_state["score"] > 100:
        risk_state["score"] = 100

    classify_risk(details)

def classify_risk(details):
    score = risk_state["score"]

    if score >= 80:
        level = "CRITICAL"
    elif score >= 50:
        level = "HIGH"
    elif score >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"

    log_event(
        event_type="RISK_LEVEL_UPDATED",
        details={
            "risk_score": score,
            "risk_level": level,
            "trigger_events": risk_state["events"]
        },
        severity=level
    )
