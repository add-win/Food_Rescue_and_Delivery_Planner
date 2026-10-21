# Food Rescue and Delivery Planner
**Course:** CST401 Artificial Intelligence (KTU, 2019 Scheme)  
**Academic year:** 2026–2027  
**SDGs:** SDG 2 — Zero Hunger; SDG 12 — Responsible Consumption and Production

## Problem
Use AI techniques to plan the allocation and routing of synthetic surplus-food donations to community kitchens before expiry.

## CO mapping
- **CO1:** Intelligent agent and PEAS description — `agent/agent.py`
- **CO2:** Uniform-Cost Search and A* — `search/`
- **CO3:** Backtracking CSP and forward checking — `csp/`
- **CO4:** Knowledge-base rules and reasoning trace — `logic/`

## Requirements
- Python 3.10+
- Optional: `pip install -r requirements.txt` for pytest

## Run
From the project root:
```bash
python main.py
python main.py normal
python main.py tight
python main.py changed
python main.py failure
```

## Tests
```bash
python -m pytest -q
```

## Data and assumptions
All data is synthetic. Road edge weights are abstract distance/cost units. Dairy requires a kitchen with cold storage. Cooked food with at most 2 hours to expiry is critical; up to 5 hours is high urgency. The current prototype allocates donations and plans each assigned donation route independently; it does not simulate a shared multi-stop tour or exact travel-time/expiry feasibility.

## Team
Addwin Alanolikkal (CCE23CS006)
Abel J Kolapran (CCE23CS001)
Abhay Achuthan R (CCE23CS002)
Abhijith P S (CCE23CS004)
Abhinav C M (CCE23CS005)
Abhijith C S (CCE23CS003)