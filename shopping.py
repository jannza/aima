# -*- coding: utf-8 -*-


from search_mod import *

class ShoppingProblem(GraphProblem):
    
 
    on_sale = {'A':('siider', 'kohupiim'), 'B':('tapeet', 'liim'),
                  'C':('juust ', 'hakkliha'), 'D':('arbuus', 'kohv'),
                  'E':('pirukas', 'piim'), 'F':('kassiliiv', 'mahl'),
                  'G':('arbuus', 'kohv'), 'H':('kassiliiv', 'mahl'),
                  'I':('polt', 'mutter'), 'J':('siider', 'kohupiim'),
                  'K':('pirukas', 'piim'), 'L':('juust', 'hakkliha'),
                  'M':('juust', 'hakkliha'), 'N':('siider', 'kohupiim'),
                  'O':('tapeet', 'liim'), 'P':('pirukas', 'piim'),
                  'R':('sai', 'leib'), 'S':('vorst', 'banaan'),
                  'T':('valgusti', 'metall'), 'U':('vorst', 'banaan'), 
                  'V':('sai', 'leib')                   
    }
    

    def __init__(self, initial, graph, goal):
        Problem.__init__(self, initial, goal)
        self.basket = []
        self.graph = graph
        self.goal = list(goal)
        self.still_need = list(goal)
        
        
    def actions(self, state):
        "The actions at a graph node are just its neighbors."
        return self.graph.get(state).keys()
    
    def result(self, state, action):
        "The result of going to a neighbor is just that neighbor."
        return action
    
    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or infinity)
    
    
    def goal_test(self, node):
        # items that can be bought on the way
        combined_basket = []
        # just in case
        local_goal = list(self.goal)
        # iterate path to buy items
        for node in node.path():
            for i in local_goal:
                for j in self.on_sale.get(node.state):
                    if i == j:
                        combined_basket.append(i)
                        local_goal.remove(i)
        # check if everything can be bought
        if sorted(self.goal) == sorted(combined_basket):
            return True
        else:            
            return False
    
    def h_my(self, node):
        # just in case
        local_goal = list(self.goal)
        # everything bought before last step
        previously_bought = []     
        # get previously bought items
        for a in range(len(node.path()) - 1):
            for i in local_goal:
                for j in self.on_sale.get(node.path()[a].state):
                    if i == j:
                        previously_bought.append(i)
                        local_goal.remove(i)
        # get items what are still not bought
        need = list(set(self.goal) - set(previously_bought))
        result = len(need)
        # check what can be bought from this shop
        for i in need:
                for j in self.on_sale.get(node.state):
                    if i == j:
                        result = result - 1
               
        helper = (float(result) / len(local_goal))
        helper = (int)(helper * 100)
        # add distance to equation
        current = node.state
        if len(node.path()) > 1:
            last = node.path()[-2].state 
            dist = self.graph.get(current, last)
        else:
            dist = 10000            
            
        if len(need) == result:
            result = 500000
        else:
            result = helper * dist
        return result

    def hzero(self, node):
        return 0

shops = UndirectedGraph(Dict(
    A=Dict(D=600, H=3700),
    B=Dict(C=2000, I=1700, L=2300),
    C=Dict(E=1200, F=3500, G=2900),
    D=Dict(G=3500),
    E=Dict(F=2400, J=5300),
    F=Dict(J=6000),
    G=Dict(I=1900),
    H=Dict(I=2100, L=1800),
    J=Dict(K=5100),
    K=Dict(L=5000)))
    
improved_shops = UndirectedGraph(Dict(
    A=Dict(B=600, E=2300, K=3700),
    B=Dict(C=1400, E=3500),
    C=Dict(D=2800, E=2300),
    D=Dict(E=1400, F=1400, G=2000, H=2700),
    E=Dict(F=1700, I=1900),
    F=Dict(G=1400, I=2400, L=2700),
    G=Dict(H=2100, J=1200),
    H=Dict(P=2300),
    I=Dict(L=1000, N=1900),
    J=Dict(N=1800, O=1200),
    K=Dict(L=1300, M=2100, R=1800),
    L=Dict(N=1600),
    M=Dict(R=1800),
    N=Dict(R=2300),
    O=Dict(P=2400, T=5300),
    P=Dict(T=6000),
    R=Dict(S=1400),
    S=Dict(U=2300),
    T=Dict(V=4200),
    U=Dict(V=2400)))


if __name__ == "__main__":
    random = ['kohupiim','piim','mahl','tapeet']
    random2 = ['piim','juust','kassiliiv','kohv']
    first = ['A','B','E','F','G','J','O','T']
    second = ['D','G','H','K','M','R','S','U']
    
    for a in first:
        f = ShoppingProblem(a, improved_shops, random)
        print('Starting from '+f.initial+ ' have to buy ' + str(random))
        compare2(f, searchers=[astar_search, recursive_best_first_search], heuristics =[f.h_my, f.hzero])
        print('astar+h_my path '+str(astar_search(f, f.h_my).solution()))
        
        
        print('----------------------------------------------------------------------')
    
    for a in second:
        f = ShoppingProblem(a, improved_shops, random2)
        print('Starting from '+f.initial+ ' have to buy ' + str(random2))
        compare2(f, searchers=[astar_search, recursive_best_first_search], heuristics =[f.h_my, f.hzero])
        
        print('astar+h_my path '+str(astar_search(f, f.h_my).solution()))
        print('----------------------------------------------------------------------')
        



    






