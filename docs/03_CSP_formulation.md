# CO3 — CSP Formulation

**Variables:** one variable per donation.  
**Domain:** compatible (vehicle, kitchen) pairs.  
**Constraints:** vehicle must be available; donation weight must fit vehicle capacity; total assigned weight must fit kitchen capacity; kitchen must need the food type; dairy requires cold storage.  
**Methods:** recursive backtracking and a forward-checking variant that removes assignments incompatible with remaining capacities. If not all donations can be assigned, the prototype reports them as UNASSIGNED rather than crashing.
