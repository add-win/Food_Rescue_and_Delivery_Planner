"""CO1 intelligent-agent description and orchestration helpers. Roles: Members 1 and 2."""

PEAS = {
    "Performance": "Kilograms delivered before expiry, kitchens served, route distance, waste avoided.",
    "Environment": "Synthetic providers, donations, community kitchens, vehicles and weighted roads.",
    "Actuators": "Assign donations, select kitchens and vehicles, produce delivery routes and reports.",
    "Sensors": "Donation type/weight/expiry, kitchen needs/storage/capacity, vehicle capacity/availability, road costs."
}

def describe_agent():
    print("\n=== CO1: INTELLIGENT AGENT / PEAS ===")
    for key, value in PEAS.items():
        print(f"{key}: {value}")
    print("Task environment: partially observable, sequential, dynamic, discrete, multi-agent environment;")
    print("planning is deterministic for a fixed synthetic input.")
