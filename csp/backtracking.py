"""Backtracking CSP allocator. Role: Member 4 (CO3)."""

def candidates_for(donation, kitchens, vehicles):
    candidates = []
    for kitchen in kitchens:
        from logic.kb import is_eligible
        if not is_eligible(donation, kitchen):
            continue
        for vehicle in vehicles:
            if vehicle["available"] and donation["kg"] <= vehicle["capacity_kg"]:
                candidates.append((vehicle["id"], kitchen["id"]))
    return candidates

def allocate_backtracking(donations, kitchens, vehicles):
    """Assign each eligible donation to (vehicle, kitchen), or None if unassigned."""
    domains = {d["id"]: candidates_for(d, kitchens, vehicles) for d in donations}
    # Critical and constrained donations are considered first.
    ordered = sorted(donations, key=lambda d: (
        len(domains[d["id"]]), d["hours_to_expiry"], -d["kg"]))
    vehicle_by_id = {v["id"]: v for v in vehicles}
    kitchen_by_id = {k["id"]: k for k in kitchens}
    used_vehicle = {v["id"]: 0 for v in vehicles}
    used_kitchen = {k["id"]: 0 for k in kitchens}
    assignment = {}
    attempts = 0

    def search(index):
        nonlocal attempts
        if index == len(ordered):
            return True
        donation = ordered[index]
        did = donation["id"]
        # If no valid domain, leave it unassigned and continue safely.
        if not domains[did]:
            assignment[did] = None
            return search(index + 1)
        for vid, kid in domains[did]:
            attempts += 1
            vehicle = vehicle_by_id[vid]
            kitchen = kitchen_by_id[kid]
            if used_vehicle[vid] + donation["kg"] > vehicle["capacity_kg"]:
                continue
            if used_kitchen[kid] + donation["kg"] > kitchen["capacity_kg"]:
                continue
            assignment[did] = {"vehicle": vid, "kitchen": kid}
            used_vehicle[vid] += donation["kg"]
            used_kitchen[kid] += donation["kg"]
            if search(index + 1):
                return True
            used_vehicle[vid] -= donation["kg"]
            used_kitchen[kid] -= donation["kg"]
            assignment.pop(did, None)
        # Allow a donation to remain unassigned if capacity constraints prevent it.
        assignment[did] = None
        if search(index + 1):
            return True
        assignment.pop(did, None)
        return False

    search(0)
    return assignment, attempts
