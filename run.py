# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
nodo, cuenta=search.breadth_first_graph_search(ab)
print("Camino recorrido", nodo.path(), "Nodos expandidos:", cuenta)
print("**************************")
s2=search.depth_first_graph_search(ab)
print("Camino recorrido", nodo.path(), "Nodos expandidos:", cuenta)
print("**************************")
s3=search.branch_and_bound_graph_search(ab)
print("Camino recorrido", nodo.path(), "Nodos expandidos:", cuenta)


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
