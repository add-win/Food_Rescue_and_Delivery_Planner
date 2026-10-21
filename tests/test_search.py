import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from search.ucs import uniform_cost_search
from search.astar import astar_search

def test_ucs_and_astar_find_same_optimal_cost():
    graph = {"A":{"B":2,"C":5}, "B":{"A":2,"C":1}, "C":{"A":5,"B":1}}
    assert uniform_cost_search(graph, "A", "C")["cost"] == 3
    assert astar_search(graph, "A", "C")["cost"] == 3
