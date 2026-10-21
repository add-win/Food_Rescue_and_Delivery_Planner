"""Backtracking with forward checking. Role: Member 4 (CO3)."""
from logic.kb import is_eligible

def allocate_forward_checking(donations, kitchens, vehicles):
    vehicle_by_id = {v["id"]: v for v in vehicles}
    kitchen_by_id = {k["id"]: k for k in kitchens}
    domains = {}
    for d in donations:
        domains[d["id"]] = [
            (v["id"], k["id"])
            for v in vehicles if v["available"] and d["kg"] <= v["capacity_kg"]
            for k in kitchens if is_eligible(d, k)
        ]
    ordered = sorted(donations, key=lambda d: (len(domains[d["id"]]), d["hours_to_expiry"]))
    remaining_v = {v["id"]: v["capacity_kg"] for v in vehicles}
    remaining_k = {k["id"]: k["capacity_kg"] for k in kitchens}
    assignment, attempts = {}, 0

    def search(index, current_domains):
        nonlocal attempts
        if index == len(ordered):
            return True
        d = ordered[index]
        did = d["id"]
        if not current_domains[did]:
            assignment[did] = None
            return search(index + 1, current_domains)
        for vid, kid in current_domains[did]:
            attempts += 1
            if d["kg"] > remaining_v[vid] or d["kg"] > remaining_k[kid]:
                continue
            assignment[did] = {"vehicle": vid, "kitchen": kid}
            remaining_v[vid] -= d["kg"]
            remaining_k[kid] -= d["kg"]
            # Forward checking: remove choices that exceed any remaining capacity.
            next_domains = {key: list(value) for key, value in current_domains.items()}
            failed = False
            for future in ordered[index + 1:]:
                fid = future["id"]
                next_domains[fid] = [
                    (v, k) for v, k in next_domains[fid]
                    if future["kg"] <= remaining_v[v] and future["kg"] <= remaining_k[k]
                ]
                if not next_domains[fid]:
                    # Empty domain means the item can be left unassigned; do not crash.
                    continue
            if search(index + 1, next_domains):
                return True
            remaining_v[vid] += d["kg"]
            remaining_k[kid] += d["kg"]
            assignment.pop(did, None)
        assignment[did] = None
        if search(index + 1, current_domains):
            return True
        assignment.pop(did, None)
        return False

    search(0, domains)
    return assignment, attempts
