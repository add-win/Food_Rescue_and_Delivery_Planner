# CSP Results

Captured from the `tight` scenario. The CLI displays the backtracking
assignment. Both allocator functions were also invoked directly to compare
their returned assignments.

| Donation | Weight | Backtracking assignment | Forward-checking assignment |
|---|---:|---|---|
| D1 | 12 kg | V2 -> K3 | V2 -> K3 |
| D2 | 10 kg | UNASSIGNED | UNASSIGNED |
| D3 | 8 kg | V1 -> K2 | V1 -> K2 |
| D4 | 7 kg | UNASSIGNED | UNASSIGNED |
| D5 | 6 kg | V1 -> K1 | V1 -> K1 |

| Method | Assignment attempts |
|---|---:|
| Backtracking | 20 |
| Forward checking | 3 |

Both methods returned the same assignment: **26 kg assigned out of 43 kg**,
with D2 and D4 unassigned under the tight capacities. Attempt counts are the
candidate assignments tried by the implementation, not the number of search
tree nodes.
