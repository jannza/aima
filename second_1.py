import logic
import itertools


def solve(steps):
    for moves in  range(0, steps+1):
        

        print("trying with "+str(moves)+" moves")
        KB = logic.PropKB()
        
        #initial state
        KB.tell(logic.expr("~At_0(Spare, Ground)"))
        KB.tell(logic.expr("At_0(Spare, Trunk)"))
        KB.tell(logic.expr("~At_0(Spare, Axle)"))
        KB.tell(logic.expr("At_0(Flat, Axle)"))
        KB.tell(logic.expr("~At_0(Flat, Ground)"))
        KB.tell(logic.expr("~At_0(Flat, Trunk)"))
        
        
        #first preconditions
        
        
        for i in range(0,moves):
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Trunk) | At_"+str(i)+"(Spare, Trunk)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Spare, Axle) | At_"+str(i)+"(Spare, Ground)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Spare, Axle) | ~At_"+str(i)+"(Flat, Axle) "))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Axle) | At_"+str(i)+"(Spare, Axle)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Axle) | At_"+str(i)+"(Flat, Axle)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Flat, Axle) | At_"+str(i)+"(Flat, Ground) "))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Flat, Axle) | ~At_"+str(i)+"(Flat, Axle) "))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Trunk) | At_"+str(i)+"(Flat, Trunk)"))
        
        
        
        #second positive effects
        for i in range(0,moves):
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Trunk) | At_"+str(i+1)+"(Spare, Ground)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Spare, Axle) | At_"+str(i+1)+"(Spare, Axle)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Axle) | At_"+str(i+1)+"(Spare, Ground)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Axle) | At_"+str(i+1)+"(Flat, Ground)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Flat, Axle) | At_"+str(i+1)+"(Flat, Axle)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Trunk) | At_"+str(i+1)+"(Flat, Ground)"))
        
        
        
        #third negative effects
        
        for i in range(0,moves):
        
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Trunk) | ~At_"+str(i+1)+"(Spare, Trunk)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Spare, Axle) | ~At_"+str(i+1)+"(Spare, Ground)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Spare, Axle) | ~At_"+str(i+1)+"(Spare, Axle)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Axle) | ~At_"+str(i+1)+"(Flat, Axle)"))
            KB.tell(logic.expr("~PutOn_"+str(i)+"(Flat, Axle) | ~At_"+str(i+1)+"(Flat, Ground)"))
            KB.tell(logic.expr("~Remove_"+str(i)+"(Flat, Trunk) | ~At_"+str(i+1)+"(Flat, Trunk)"))
            
            
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Spare, Ground)"))
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Spare, Axle)"))
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Spare, Trunk)"))
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Flat, Ground)"))
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Flat, Axle)"))
            KB.tell(logic.expr("~LeaveOvernight_"+str(i)+" | ~At_"+str(i+1)+"(Flat, Trunk)"))
        
        
        
        #fourth from false to true
        
        for i in range(0,moves):
            KB.tell(logic.expr("At_"+str(i)+"(Spare, Ground) | ~At_"+str(i+1)+"(Spare, Ground) | Remove_"+str(i)+"(Spare, Trunk) | Remove_"+str(i)+"(Spare, Axle)"))
            KB.tell(logic.expr("At_"+str(i)+"(Spare, Trunk) | ~At_"+str(i+1)+"(Spare, Trunk)"))
            KB.tell(logic.expr("At_"+str(i)+"(Spare, Axle) | ~At_"+str(i+1)+"(Spare, Axle) | PutOn_"+str(i)+"(Spare, Axle)"))
            KB.tell(logic.expr("At_"+str(i)+"(Flat, Axle) | ~At_"+str(i+1)+"(Flat, Axle) | PutOn_"+str(i)+"(Flat, Axle)"))
            KB.tell(logic.expr("At_"+str(i)+"(Flat, Ground) | ~At_"+str(i+1)+"(Flat, Ground) | Remove_"+str(i)+"(Flat, Axle) | Remove_"+str(i)+"(Flat, Trunk)"))
            KB.tell(logic.expr("At_"+str(i)+"(Flat, Trunk) | ~At_"+str(i+1)+"(Flat, Trunk)"))
        
        
        
        #fifth from true to false
        for i in range(0,moves):
            KB.tell(logic.expr("~At_"+str(i)+"(Spare, Ground) | At_"+str(i+1)+"(Spare, Ground) | PutOn_"+str(i)+"(Spare, Axle) | LeaveOvernight_"+str(i)+""))
            KB.tell(logic.expr("~At_"+str(i)+"(Spare, Trunk) | At_"+str(i+1)+"(Spare, Trunk) | Remove_"+str(i)+"(Spare, Trunk) | LeaveOvernight_"+str(i)+""))
            KB.tell(logic.expr("~At_"+str(i)+"(Spare, Axle) | At_"+str(i+1)+"(Spare, Axle) | Remove_"+str(i)+"(Spare, Axle)  | LeaveOvernight_"+str(i)+""))
            KB.tell(logic.expr("~At_"+str(i)+"(Flat, Axle) | At_"+str(i+1)+"(Flat, Axle) | Remove_"+str(i)+"(Flat, Axle) | LeaveOvernight_"+str(i)+""))
            KB.tell(logic.expr("~At_"+str(i)+"(Flat, Ground) | At_"+str(i+1)+"(Flat, Ground) | PutOn_"+str(i)+"(Flat, Axle) | LeaveOvernight_"+str(i)+""))
            KB.tell(logic.expr("~At_"+str(i)+"(Flat, Trunk) | At_"+str(i+1)+"(Flat, Trunk) | Remove_"+str(i)+"(Flat, Trunk) | LeaveOvernight_"+str(i)+""))
            
        
        #list of all possible actions
        #actions without timestamp, will be added later
        
        actions = ["Remove_(Spare, Trunk)", "PutOn_(Spare, Axle)", "Remove_(Spare, Axle)", 
                   "Remove_(Flat, Axle)", "PutOn_(Flat, Axle)", "Remove_(Flat, Trunk)", "LeaveOvernight_"]
        
        
        
        #sixth, only one action can take place
        
        for i in range(0,moves):
            for elem in itertools.combinations(actions, 2):
                KB.tell(logic.expr("~"+elem[0].replace("_","_"+str(i))+" | ~"+elem[1].replace("_","_"+str(i))))
        
        
        
        #seventh, one action must take place
        
        for i in range(0,moves):
            seventh = ""
            for elem in actions:    
                seventh += elem.replace("_","_"+str(i)) + " | " 
            seventh = seventh[:-2]
            KB.tell(logic.expr(seventh))
        
        
        
        #add goal
        KB.tell(logic.expr("At_"+str(moves)+"(Spare, Axle)"))
        
        
        
        #some manual cnf just to be sure
        string = ""
        for elem in KB.clauses:
            elem = logic.to_cnf(str(elem))
            string = string + str(elem) + " & "
            
        string = string[:-2]    
        
        
        action_stubs = ["Remove", "PutOn", "LeaveOvernight"]
        
        
        
        #print only true values
        answer = logic.dpll_satisfiable(logic.expr(string))
        if answer == False:
            print("Couldn't solve problem in "+str(moves)+" turns")
        else:
            print("Found solution with "+str(moves)+" turns")
            for elem in answer:
                if answer[elem]:
                    if any(sub in str(elem) for sub in action_stubs):
                        print(str(elem)+ " : " +str(answer[elem]))
            break


solve(3)


