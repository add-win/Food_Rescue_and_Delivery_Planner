"""Food Rescue and Delivery Planner: integrated CST401 prototype.
Integration role: Member 1. All data is synthetic.
"""
import json
import sys
from pathlib import Path
from agent.agent import describe_agent
from logic.inference import evaluate_donations, query_critical
from csp.backtracking import allocate_backtracking
from csp.propagation import allocate_forward_checking
from search.ucs import uniform_cost_search
from search.astar import astar_search

ROOT = Path(__file__).resolve().parent

def load_scenarios():
    with (ROOT / "data" / "scenarios.json").open(encoding="utf-8") as file:
        return json.load(file)

def build_graph(roads, closed_roads=None):
    graph = {}
    closed = {frozenset(edge) for edge in (closed_roads or [])}
    for a, b, cost in roads:
        if frozenset((a, b)) in closed:
            continue
        graph.setdefault(a, {})[b] = cost
        graph.setdefault(b, {})[a] = cost
    return graph

def route_for_assignment(graph, donation, kitchen_id):
    provider = donation["provider"]
    first = uniform_cost_search(graph, "DEPOT", provider)
    second = uniform_cost_search(graph, provider, kitchen_id)
    if not first["path"] or not second["path"]:
        return None
    return {
        "path": first["path"][:-1] + second["path"],
        "cost": first["cost"] + second["cost"],
        "ucs_nodes": first["nodes_expanded"] + second["nodes_expanded"]
    }

def run_scenario(name, scenario):
    print("\n" + "=" * 72)
    print(f"SCENARIO: {name.upper()} — {scenario['description']}")
    print("=" * 72)
    donations = scenario["donations"]
    kitchens = scenario["kitchens"]
    vehicles = [
        {**v, "available": v["available"] and v["id"] not in scenario.get("unavailable_vehicles", [])}
        for v in scenario["vehicles"]
    ]
    graph = build_graph(scenario["roads"], scenario.get("closed_roads", []))

    # CO1: perceive the environment and state the agent model.
    describe_agent()

    # CO4: apply rules and show the reasoning trace.
    evaluated, trace = evaluate_donations(donations, kitchens)
    print("\n=== CO4: KNOWLEDGE-BASE REASONING TRACE ===")
    for line in trace:
        print(line)
    print("Query 1 — Critical donations:", query_critical(donations))
    d3 = next((d for d in donations if d["id"] == "D3"), None)
    k2 = next((k for k in kitchens if k["id"] == "K2"), None)
    if d3 and k2:
        from logic.inference import query_deliverable
        print(f"Query 2 — Is D3 deliverable to K2? {query_deliverable(d3, k2)}")

    # CO3: solve CSP using backtracking and forward checking.
    assignment, attempts_bt = allocate_backtracking(donations, kitchens, vehicles)
    assignment_fc, attempts_fc = allocate_forward_checking(donations, kitchens, vehicles)
    print("\n=== CO3: CSP ALLOCATION ===")
    print("Backtracking assignments tried:", attempts_bt)
    print("Forward-checking assignments tried:", attempts_fc)
    delivered_kg = 0
    for donation in donations:
        allocation = assignment.get(donation["id"])
        if allocation:
            delivered_kg += donation["kg"]
            print(f"{donation['id']} ({donation['kg']} kg) -> vehicle "
                  f"{allocation['vehicle']} -> kitchen {allocation['kitchen']}")
        else:
            print(f"{donation['id']} ({donation['kg']} kg) -> UNASSIGNED")
    if assignment != assignment_fc:
        print("Note: CSP methods may choose different valid assignments; inspect both if comparing.")

    # CO2: compare UCS and A* on identical provider-to-kitchen route segments.
    print("\n=== CO2: SEARCH COMPARISON ===")
    total_cost, total_nodes = 0, 0
    for donation in donations:
        allocation = assignment.get(donation["id"])
        if not allocation:
            continue
        provider = donation["provider"]
        kitchen = allocation["kitchen"]
        ucs = uniform_cost_search(graph, provider, kitchen)
        astar = astar_search(graph, provider, kitchen)  # zero heuristic is admissible
        print(f"{donation['id']}: {provider} -> {kitchen}")
        print(f"  UCS:  path={ucs['path']} cost={ucs['cost']} nodes={ucs['nodes_expanded']}")
        print(f"  A*:   path={astar['path']} cost={astar['cost']} nodes={astar['nodes_expanded']}")
        route = route_for_assignment(graph, donation, kitchen)
        if route:
            total_cost += route["cost"]
            total_nodes += route["ucs_nodes"]
            print(f"  Full route from depot: {route['path']} cost={route['cost']}")
        else:
            print("  Route unavailable due to disconnected road graph.")

    print("\n=== PERFORMANCE SUMMARY ===")
    print(f"Total donation weight: {sum(d['kg'] for d in donations)} kg")
    print(f"Weight assigned (not a physical dispatch confirmation): {delivered_kg} kg")
    print(f"Donations assigned: {sum(1 for x in assignment.values() if x)} / {len(donations)}")
    print(f"Combined estimated route cost for assigned donations: {total_cost}")
    print("Metric note: road edge costs are synthetic distance units; routes are planned independently.")
    print("Limitations: no real-time traffic, exact delivery-time simulation, or shared multi-stop vehicle tour.")

def main():
    scenarios = load_scenarios()
    names = list(scenarios)
    selected = sys.argv[1].lower() if len(sys.argv) > 1 else "all"
    if selected == "all":
        for name in names:
            run_scenario(name, scenarios[name])
    elif selected in scenarios:
        run_scenario(selected, scenarios[selected])
    else:
        print("Usage: python main.py [all|normal|tight|changed]")
        raise SystemExit(2)

if __name__ == "__main__":
    main()
