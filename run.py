# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
tv = search.GPSProblem('T', 'V', search.romania)
uz = search.GPSProblem('U', 'Z', search.romania)

node,count=search.breadth_first_graph_search(ab)
print("Camino recorrido anchura", node.path(), "Nodos visitados:", count)
print("**************************")
node,count=search.depth_first_graph_search(ab)
print("Camino recorrido profundidad", node.path(), "Nodos visitados:", count)
print("**************************")

node,count=search.branch_and_bound_graph_search(ab)
print("Camino recorrido ramificación y acotación A-B", node.path(), "Nodos visitados:", count)
print("**************************")
node,count=search.branch_and_bound_subestimation_graph_search(ab)
print("Camino recorrido ramificación y acotación con subestimación A-B", node.path(), "Nodos visitados:", count)
print("**************************")

node,count=search.branch_and_bound_graph_search(tv)
print("Camino recorrido ramificación y acotación T-V", node.path(), "Nodos visitados:", count)
print("**************************")
node,count=search.branch_and_bound_subestimation_graph_search(tv)
print("Camino recorrido ramificación y acotación con subestimación T-V", node.path(), "Nodos visitados:", count)
print("**************************")

node,count=search.branch_and_bound_graph_search(uz)
print("Camino recorrido ramificación y acotación U-Z", node.path(), "Nodos visitados:", count)
print("**************************")
node,count=search.branch_and_bound_subestimation_graph_search(uz)
print("Camino recorrido ramificación y acotación con subestimación U-Z", node.path(), "Nodos visitados:", count)
print("**************************")



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
