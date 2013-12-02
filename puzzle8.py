#from search import Problem
from search import *

class puzzle(Problem):
    goal = (1,2,3,4,5,6,7,8,0)
    
    def __init__(self, initial):
        self.initial = initial
    
    def actions(self, state):
        possible = []
        loc = state.index(0)
        if loc -3 >= 0:
            possible.append((loc -3))
        if loc -1 >= 0:
            possible.append((loc -1))
        if loc +1 <= 8:
            possible.append((loc +1))
        if loc +3 <= 8:
            possible.append((loc +3))
        return possible
   
    def result(self, state, move):
        
        new = list(state)
        inside = state[move]
        loc = new.index(0)
        new[loc] = inside
        new[move]= 0
        #print state
        #print new
        return tuple(new)
    
    
    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False
    
    
    def h(self, state):
        #print node 
        #print state
        misplaced = 0
#         print(len(state.state))
        for i in range(len(state.state)):
            if state.state[i] != self.goal[i]:
                misplaced = misplaced +1
        
#         print misplaced
        return 0
        

        
    
if __name__ == "__main__":
    #f = puzzle(Problem)
    #print f.actions([1,2,3,4,0,5,6,7,8])
    
    
    #print depth_first_tree_search(puzzle((1,2,3,4,5,6,7,0,8)))
    #print breadth_first_tree_search(puzzle((1,2,3,4,5,6,7,0,8)))
    
    
      
    compare_searchers(problems=[puzzle((1,2,3,4,5,0,6,7,8))],
            header=['Searcher', 'puzzle'])
   
   
   
   
#     compare_searchers(problems=[GraphProblem('A', 'B', romania),
#                                 GraphProblem('O', 'N', romania),
#                                 GraphProblem('Q', 'WA', australia)],
#             header=['Searcher', 'Romania(A, B)', 'Romania(O, N)', 'Australia'])