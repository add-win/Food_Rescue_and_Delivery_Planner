# CO1 — PEAS and Architecture

| PEAS element | Description |
|---|---|
| Performance | Maximize kg delivered before expiry and kitchens served; reduce route cost and food waste. |
| Environment | Synthetic providers, donations, kitchens, vehicles and weighted road graph. |
| Actuators | Assign donations, choose vehicle/kitchen, produce route and report. |
| Sensors | Food type, kg, expiry, kitchen needs/storage/capacity, vehicle capacity/availability, roads. |

**Environment classification:** partially observable (the prototype sees only supplied data); sequential; dynamic in the real world; discrete; deterministic for fixed input; multi-agent environment (providers, drivers and kitchens), while the prototype planner itself is a single planning agent.

**Architecture:** Input data → CO4 eligibility/urgency rules → CO3 CSP allocation → CO2 route search → CO1 report and performance summary.
