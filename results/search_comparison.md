# Search Comparison

Run performed with `python main.py normal`. The route search compares the
same provider-to-assigned-kitchen segment using UCS and A*. A* uses the
default zero heuristic, so it behaves like UCS for these routes.

| Donation | Segment | UCS path | UCS cost | UCS nodes | A* path | A* cost | A* nodes | Full depot route cost |
|---|---|---|---:|---:|---|---:|---:|---:|
| D1 | P1 -> K1 | P1 -> K1 | 2 | 3 | P1 -> K1 | 2 | 3 | 4 |
| D2 | P2 -> K2 | P2 -> K2 | 2 | 3 | P2 -> K2 | 2 | 3 | 5 |
| D3 | P3 -> K2 | P3 -> K2 | 2 | 2 | P3 -> K2 | 2 | 2 | 6 |
| D4 | P4 -> K1 | P4 -> K1 | 3 | 4 | P4 -> K1 | 3 | 4 | 5 |
| D5 | P5 -> K1 | P5 -> K1 | 2 | 2 | P5 -> K1 | 2 | 2 | 5 |

For every segment, UCS and A* returned the same optimal cost and path, and
expanded the same number of nodes. The full routes from the depot were
`DEPOT -> P1 -> K1`, `DEPOT -> P2 -> K2`, `DEPOT -> P3 -> K2`,
`DEPOT -> P4 -> K1`, and `DEPOT -> P5 -> K1`. Their combined estimated
cost is **25 synthetic distance units**.

The full route cost includes the depot-to-provider leg; the table's UCS/A*
comparison is specifically provider-to-kitchen.
