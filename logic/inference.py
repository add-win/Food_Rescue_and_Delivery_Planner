"""Simple forward-chaining-style rule evaluation with reasoning trace. Role: Member 5 (CO4)."""
from logic.kb import facts_for, is_eligible, urgency

def evaluate_donations(donations, kitchens):
    results = []
    trace = []
    for donation in donations:
        facts = facts_for(donation, kitchens)
        trace.append(f"FACT: {donation['id']} is {donation['food_type']}, "
                     f"{donation['kg']} kg, expires in {donation['hours_to_expiry']} hours.")
        trace.append(f"RULE urgency: {donation['id']} -> {facts['urgency']} "
                     f"(expiry threshold applied).")
        if facts["eligible_kitchens"]:
            trace.append(f"RULE eligibility: {donation['id']} can be delivered to "
                         f"{', '.join(facts['eligible_kitchens'])}.")
        else:
            trace.append(f"RULE eligibility: {donation['id']} has NO compatible kitchen.")
        results.append({**donation, **facts})
    return results, trace

def query_critical(donations):
    """Query 1: Which donations are critical?"""
    return [d["id"] for d in donations if urgency(d) == "CRITICAL"]

def query_deliverable(donation, kitchen):
    """Query 2: Is this donation deliverable to this kitchen?"""
    return is_eligible(donation, kitchen)
