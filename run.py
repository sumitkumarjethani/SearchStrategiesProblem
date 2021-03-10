# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
s1=search.breadth_first_graph_search(ab)
print("Camino recorrido", s1[0].path(), "Nodos expandidos:", s1[1])
print("**************************")
s2=search.depth_first_graph_search(ab)
print("Camino recorrido", s2[0].path(), "Nodos expandidos:", s2[1])
print("**************************")
s3=search.branch_and_bound_graph_search(ab)
print("Camino recorrido", s3[0].path(), "Nodos expandidos:", s3[1])


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
