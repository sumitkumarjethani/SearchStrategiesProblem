SearchStrategiesProblem

Search algorithms perform path discovery, preferably optimal, in graphs. We will code how to carry out a search line in different ways: first in depth, first in width, branch and bound...

The branching and bounding search strategy belongs to the uninformed search strategies. Its operating principle is based on ordering the open list taking as a criterion the accumulated cost of each partial trajectory, represented by each node of the open list. Therefore, the first node in the list will expand and generate new trajectories by branching its children.