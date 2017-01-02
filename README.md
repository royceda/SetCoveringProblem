
# SetCoveringProblem
Set Covering Problem (SCP) is a classical problem of the Operation Reaserch (OR) which has many applications.

## Description
Given:
* m items i \in I={1,2, m}
* n subset P_j such as P_j in I whose the cost is c_j > 0
* t_ij = 1 if i in P_j ( else t_ij = 0)

A cover of I is the set {P_j, j in K included in J) such as Union(P_j, j) = I

The problem is the following:

min sum(c_j * x_j, j in J)
st { sum(t_ij*x_j >= 1) forall i in I, x_j in {0,1} forall j in J)}

## Solving
1. Preprocessing to reduce the problem
2. Heuristic primal to get a Lower Bound
3. Heuristic Dual to get a Upper Bound 

## Preprocessing
* Rule 1:
* Rule 2:
* Rule 3:
* Rule 4:

## Heurisitic primal

## Heuristic Dual

# Bibliography
