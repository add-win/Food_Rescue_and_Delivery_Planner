# Test Results

## Verification performed

Commands run from the project root:

```text
python main.py all
python -m pytest -q
```

Both commands exited successfully. Pytest reported **3 passed in 0.02s**. The
integrated run exercised `normal`, `tight`, `changed`, and `failure`.

## Scenario results

| Scenario | Weight assigned | Donations assigned | Backtracking attempts | Forward-checking attempts | Combined route cost |
|---|---:|---:|---:|---:|---:|
| `normal` | 30 / 30 kg | 5 / 5 | 9 | 5 | 25 |
| `tight` | 26 / 43 kg | 3 / 5 | 20 | 3 | 17 |
| `changed` | 16 / 30 kg | 3 / 5 | 9 | 3 | 16 |
| `failure` | 0 / 5 kg | 0 / 1 | 0 | 0 | 0 |

The normal, tight, and changed scenarios produced matching UCS and A* costs
for every assigned provider-to-kitchen segment. With the default zero
heuristic, their node-expansion counts also matched. In `tight`, D1 and D4
were classified CRITICAL; in `failure`, dairy donation D6 was left
UNASSIGNED because neither kitchen has cold storage.

Route costs are synthetic edge-cost units. The prototype plans each assigned
donation route independently; assigned weight is not a physical dispatch
confirmation.
