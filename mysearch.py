import search

ab = search.GraphProblem('A', 'B', search.romania)
print search.breadth_first_tree_search(ab).solution()