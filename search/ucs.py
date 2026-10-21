"""Uniform-Cost Search. Role: Member 3 (CO2)."""
import heapq
import itertools

def uniform_cost_search(graph, start, goal):
    counter = itertools.count()
    frontier = [(0, next(counter), start, [start])]
    best_cost = {start: 0}
    expanded = 0
    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if cost != best_cost.get(node):
            continue
        expanded += 1
        if node == goal:
            return {"path": path, "cost": cost, "nodes_expanded": expanded}
        for neighbor, weight in graph.get(node, {}).items():
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, next(counter), neighbor, path + [neighbor]))
    return {"path": [], "cost": float("inf"), "nodes_expanded": expanded}
