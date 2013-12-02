from search_mod import *
from shopping import ShoppingProblem



    def h(self, node):
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