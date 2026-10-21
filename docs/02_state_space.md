# CO2 — Search State Space

For the route subproblem, a state is the current graph node. Actions move to an adjacent node; action cost is the road-edge weight. The initial state is a provider or depot, and the goal is the assigned kitchen. UCS expands the lowest accumulated path cost. A* expands lowest g(n)+h(n). This prototype uses h(n)=0, which is admissible because it never overestimates; it is equivalent to UCS for optimality, so node counts may be similar. A future version can use straight-line distances if coordinates are supplied.
