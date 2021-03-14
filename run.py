# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
node,count=search.breadth_first_graph_search(ab)
print("Camino recorrido anchura", node.path(), "Nodos expandidos:", count)
print("**************************")
node,count=search.depth_first_graph_search(ab)
print("Camino recorrido profundidad", node.path(), "Nodos expandidos:", count)
print("**************************")
node,count=search.branch_and_bound_graph_search(ab)
print("Camino recorrido ramificación y acotación", node.path(), "Nodos expandidos:", count)
print("**************************")
node,count=search.branch_and_bound_subestimation_graph_search(ab)
print("Camino recorrido ramificación y acotación con subestimación", node.path(), "Nodos expandidos:", count)


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
