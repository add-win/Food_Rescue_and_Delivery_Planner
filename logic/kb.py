"""Knowledge base facts and rule helpers. Role: Member 5 (CO4)."""

def is_storage_compatible(donation, kitchen):
    """Dairy requires cold storage; other food types use the general rule."""
    if donation["food_type"] == "dairy" and not kitchen["cold_storage"]:
        return False
    return True

def is_food_needed(donation, kitchen):
    return donation["food_type"] in kitchen["needs"]

def is_eligible(donation, kitchen):
    return is_food_needed(donation, kitchen) and is_storage_compatible(donation, kitchen)

def urgency(donation):
    hours = donation["hours_to_expiry"]
    if hours <= 2:
        return "CRITICAL"
    if hours <= 5:
        return "HIGH"
    return "NORMAL"

def facts_for(donation, kitchens):
    return {
        "donation": donation["id"],
        "food_type": donation["food_type"],
        "hours_to_expiry": donation["hours_to_expiry"],
        "urgency": urgency(donation),
        "eligible_kitchens": [k["id"] for k in kitchens if is_eligible(donation, k)]
    }
