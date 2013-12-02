from csp import *
import time

if __name__ == "__main__":
	print("testing")
# 	start = time.time()
# 	print backtracking_search(NQueensCSP(20))
# 	end = time.time()
# 	print (end - start)
# 	starting = 250
# 	for i in range(5):
# 		print("checking with "+str(starting+i))
# 		start = time.time()
# 		print backtracking_search(NQueensCSP(starting+i), inference=forward_checking, 
# 								select_unassigned_variable=mrv, order_domain_values=lcv)
# 		end = time.time()
# 		print (end - start)


	starting = 20
	for i in range(30):
		print("checking with "+str(starting))
		start = time.time()
		print backtracking_search(NQueensCSP(starting), select_unassigned_variable=mrv, inference=forward_checking)
		end = time.time()
		print (end - start)