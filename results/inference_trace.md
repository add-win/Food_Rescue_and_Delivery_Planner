# Inference Trace

Captured from `python main.py normal`. The knowledge base applies the urgency
thresholds (at most 2 hours = CRITICAL; at most 5 hours = HIGH; otherwise
NORMAL) and checks food need plus the dairy cold-storage rule.

| Donation | Facts | Urgency conclusion | Eligible kitchens |
|---|---|---|---|
| D1 | cooked, 8 kg, expires in 3 hours | HIGH | K1, K2, K3 |
| D2 | vegetables, 6 kg, expires in 8 hours | NORMAL | K1, K2, K3 |
| D3 | dairy, 5 kg, expires in 4 hours | HIGH | K2 |
| D4 | cooked, 7 kg, expires in 1.5 hours | CRITICAL | K1, K2, K3 |
| D5 | bakery, 4 kg, expires in 10 hours | NORMAL | K1, K2 |

The emitted trace reports each donation's facts, urgency-rule result, and
eligibility-rule result. The two printed queries returned:

- Critical donations: `['D4']`
- Is D3 deliverable to K2? `True`

These results agree with `logic/kb.py`: K2 needs dairy and has cold storage;
the other kitchens do not provide a compatible dairy destination.
