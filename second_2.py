import logic
import itertools



KB = logic.PropKB()


#initial state
KB.tell(logic.expr("At_0(C1, SFO)"))
KB.tell(logic.expr("~At_0(C1, JFK)"))
KB.tell(logic.expr("At_0(C2, JFK)"))
KB.tell(logic.expr("~At_0(C2, SFO)"))
KB.tell(logic.expr("At_0(P1, SFO)"))
KB.tell(logic.expr("~At_0(P1, JFK)"))
KB.tell(logic.expr("At_0(P2, JFK)"))
KB.tell(logic.expr("~At_0(P2, SFO)"))
KB.tell(logic.expr("~In_0(C1, P1)"))
KB.tell(logic.expr("~In_0(C2, P1)"))
KB.tell(logic.expr("~In_0(C1, P2)"))
KB.tell(logic.expr("~In_0(C2, P2)"))


moves = 6

#first preconditions

for i in range(0,moves):
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P1) | At_"+str(i)+"(C1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P1) | At_"+str(i)+"(P1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P2) | At_"+str(i)+"(C1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P2) | At_"+str(i)+"(P2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P1) | At_"+str(i)+"(C1, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P1) | At_"+str(i)+"(P1, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P2) | At_"+str(i)+"(C1, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P2) | At_"+str(i)+"(P2, SFO)"))
    
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P1) | At_"+str(i)+"(C2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P1) | At_"+str(i)+"(P1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P2) | At_"+str(i)+"(C2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P2) | At_"+str(i)+"(P2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P1) | At_"+str(i)+"(C2, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P1) | At_"+str(i)+"(P1, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P2) | At_"+str(i)+"(C2, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P2) | At_"+str(i)+"(P2, SFO)"))
    
    
    
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P1) | In_"+str(i)+"(C1, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P1) | At_"+str(i)+"(P1, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P2) | In_"+str(i)+"(C1, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P2) | At_"+str(i)+"(P2, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P1) | In_"+str(i)+"(C1, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P1) | At_"+str(i)+"(P1, SFO)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P2) | In_"+str(i)+"(C1, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P2) | At_"+str(i)+"(P2, SFO)"))
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P1) | In_"+str(i)+"(C2, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P1) | At_"+str(i)+"(P1, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P2) | In_"+str(i)+"(C2, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P2) | At_"+str(i)+"(P2, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P1) | In_"+str(i)+"(C2, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P1) | At_"+str(i)+"(P1, SFO)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P2) | In_"+str(i)+"(C2, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P2) | At_"+str(i)+"(P2, SFO)"))


    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, JFK, SFO) | At_"+str(i)+"(P1, JFK)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, SFO, JFK) | At_"+str(i)+"(P1, SFO)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, JFK, SFO) | At_"+str(i)+"(P2, JFK)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, SFO, JFK) | At_"+str(i)+"(P2, SFO)"))


#second positive effects

for i in range(0, moves):    
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P1) | In_"+str(i+1)+"(C1, P1)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P2) | In_"+str(i+1)+"(C1, P2)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P1) | In_"+str(i+1)+"(C1, P1)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P2) | In_"+str(i+1)+"(C1, P2)"))
    
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P1) | In_"+str(i+1)+"(C2, P1)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P2) | In_"+str(i+1)+"(C2, P2)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P1) | In_"+str(i+1)+"(C2, P1)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P2) | In_"+str(i+1)+"(C2, P2)"))
    
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P1) | At_"+str(i+1)+"(C1, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P2) | At_"+str(i+1)+"(C1, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P1) | At_"+str(i+1)+"(C1, SFO)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P2) | At_"+str(i+1)+"(C1, SFO)"))
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P1) | At_"+str(i+1)+"(C2, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P2) | At_"+str(i+1)+"(C2, JFK)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P1) | At_"+str(i+1)+"(C2, SFO)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P2) | At_"+str(i+1)+"(C2, SFO)"))
    
    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, JFK, SFO) | At_"+str(i+1)+"(P1, SFO)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, SFO, JFK) | At_"+str(i+1)+"(P1, JFK)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, JFK, SFO) | At_"+str(i+1)+"(P2, SFO)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, SFO, JFK) | At_"+str(i+1)+"(P2, JFK)"))

#third negative effects

for i in range(0,moves):
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P1) | ~At_"+str(i+1)+"(C1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, JFK, P2) | ~At_"+str(i+1)+"(C1, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P1) | ~At_"+str(i+1)+"(C1, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C1, SFO, P2) | ~At_"+str(i+1)+"(C1, SFO)"))
    
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P1) | ~At_"+str(i+1)+"(C2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, JFK, P2) | ~At_"+str(i+1)+"(C2, JFK)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P1) | ~At_"+str(i+1)+"(C2, SFO)"))
    KB.tell(logic.expr("~Load_"+str(i)+"(C2, SFO, P2) | ~At_"+str(i+1)+"(C2, SFO)"))
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P1) | ~In_"+str(i+1)+"(C1, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, JFK, P2) | ~In_"+str(i+1)+"(C1, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P1) | ~In_"+str(i+1)+"(C1, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C1, SFO, P2) | ~In_"+str(i+1)+"(C1, P2)"))
    
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P1) | ~In_"+str(i+1)+"(C2, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, JFK, P2) | ~In_"+str(i+1)+"(C2, P2)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P1) | ~In_"+str(i+1)+"(C2, P1)"))
    KB.tell(logic.expr("~Unload_"+str(i)+"(C2, SFO, P2) | ~In_"+str(i+1)+"(C2, P2)"))

    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, JFK, SFO) | ~At_"+str(i+1)+"(P1, JFK)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P1, SFO, JFK) | ~At_"+str(i+1)+"(P1, SFO)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, JFK, SFO) | ~At_"+str(i+1)+"(P2, JFK)"))
    KB.tell(logic.expr("~Fly_"+str(i)+"(P2, SFO, JFK) | ~At_"+str(i+1)+"(P2, SFO)"))
    

#fourth from false to true

for i in range(0,moves):
    KB.tell(logic.expr("At_"+str(i)+"(C1, JFK) | ~At_"+str(i+1)+"(C1, JFK) | Unload_"+str(i)+"(C1, JFK, P1) | Unload_"+str(i)+"(C1, JFK, P2)"))
    KB.tell(logic.expr("At_"+str(i)+"(C2, JFK) | ~At_"+str(i+1)+"(C2, JFK) | Unload_"+str(i)+"(C2, JFK, P1) | Unload_"+str(i)+"(C2, JFK, P2)"))
    KB.tell(logic.expr("At_"+str(i)+"(C1, SFO) | ~At_"+str(i+1)+"(C1, SFO) | Unload_"+str(i)+"(C1, SFO, P1) | Unload_"+str(i)+"(C1, SFO, P2)"))
    KB.tell(logic.expr("At_"+str(i)+"(C2, SFO) | ~At_"+str(i+1)+"(C2, SFO) | Unload_"+str(i)+"(C2, SFO, P1) | Unload_"+str(i)+"(C2, SFO, P2)"))
    
    KB.tell(logic.expr("At_"+str(i)+"(P1, JFK) | ~At_"+str(i+1)+"(P1, JFK) | Fly_"+str(i)+"(P1, SFO, JFK)"))
    KB.tell(logic.expr("At_"+str(i)+"(P2, JFK) | ~At_"+str(i+1)+"(P2, JFK) | Fly_"+str(i)+"(P2, SFO, JFK)"))
    KB.tell(logic.expr("At_"+str(i)+"(P1, SFO) | ~At_"+str(i+1)+"(P1, SFO) | Fly_"+str(i)+"(P1, JFK, SFO)"))
    KB.tell(logic.expr("At_"+str(i)+"(P2, SFO) | ~At_"+str(i+1)+"(P2, SFO) | Fly_"+str(i)+"(P2, JFK, SFO)"))
    
    
    
    KB.tell(logic.expr("In_"+str(i)+"(C1, P1) | ~In_"+str(i+1)+"(C1, P1) | Load_"+str(i)+"(C1, JFK, P1) | Load_"+str(i)+"(C1, SFO, P1)"))
    KB.tell(logic.expr("In_"+str(i)+"(C1, P2) | ~In_"+str(i+1)+"(C1, P2) | Load_"+str(i)+"(C1, JFK, P2) | Load_"+str(i)+"(C1, SFO, P2)"))
    KB.tell(logic.expr("In_"+str(i)+"(C2, P1) | ~In_"+str(i+1)+"(C2, P1) | Load_"+str(i)+"(C2, JFK, P1) | Load_"+str(i)+"(C2, SFO, P1)"))
    KB.tell(logic.expr("In_"+str(i)+"(C2, P2) | ~In_"+str(i+1)+"(C2, P2) | Load_"+str(i)+"(C2, JFK, P2) | Load_"+str(i)+"(C2, SFO, P2)")) 







#fifth from true to false
for i in range(0,moves):
    KB.tell(logic.expr("~At_"+str(i)+"(C1, SFO) | At_"+str(i+1)+"(C1, SFO) | Load_"+str(i)+"(C1, SFO, P1) | Load_"+str(i)+"(C1, SFO, P2)"))
    KB.tell(logic.expr("~At_"+str(i)+"(C2, SFO) | At_"+str(i+1)+"(C2, SFO) | Load_"+str(i)+"(C2, SFO, P1) | Load_"+str(i)+"(C2, SFO, P2)"))
    KB.tell(logic.expr("~At_"+str(i)+"(C1, JFK) | At_"+str(i+1)+"(C1, JFK) | Load_"+str(i)+"(C1, JFK, P1) | Load_"+str(i)+"(C1, JFK, P2)"))
    KB.tell(logic.expr("~At_"+str(i)+"(C2, JFK) | At_"+str(i+1)+"(C2, JFK) | Load_"+str(i)+"(C2, JFK, P1) | Load_"+str(i)+"(C2, JFK, P2)"))
    
    KB.tell(logic.expr("~At_"+str(i)+"(P1, SFO) | At_"+str(i+1)+"(P1, SFO) | Fly_"+str(i)+"(P1, SFO, JFK)"))
    KB.tell(logic.expr("~At_"+str(i)+"(P2, SFO) | At_"+str(i+1)+"(P2, SFO) | Fly_"+str(i)+"(P2, SFO, JFK)"))
    KB.tell(logic.expr("~At_"+str(i)+"(P1, JFK) | At_"+str(i+1)+"(P1, JFK) | Fly_"+str(i)+"(P1, JFK, SFO)"))
    KB.tell(logic.expr("~At_"+str(i)+"(P2, JFK) | At_"+str(i+1)+"(P2, JFK) | Fly_"+str(i)+"(P2, JFK, SFO)"))
    
    KB.tell(logic.expr("~In_"+str(i)+"(C1, P1) | In_"+str(i+1)+"(C1, P1) | Unload_"+str(i)+"(C1, JFK, P1) | Unload_"+str(i)+"(C1, SFO, P1)"))
    KB.tell(logic.expr("~In_"+str(i)+"(C2, P1) | In_"+str(i+1)+"(C2, P1) | Unload_"+str(i)+"(C2, JFK, P1) | Unload_"+str(i)+"(C2, SFO, P1)"))
    KB.tell(logic.expr("~In_"+str(i)+"(C1, P2) | In_"+str(i+1)+"(C1, P2) | Unload_"+str(i)+"(C1, JFK, P2) | Unload_"+str(i)+"(C1, SFO, P2)"))
    KB.tell(logic.expr("~In_"+str(i)+"(C2, P2) | In_"+str(i+1)+"(C2, P2) | Unload_"+str(i)+"(C2, JFK, P2) | Unload_"+str(i)+"(C2, SFO, P2)"))




#list of all possible actions
#actions without timestamp, will be added later


actions = ["Load_(C1, JFK, P1)","Load_(C1, JFK, P2)","Load_(C1, SFO, P1)","Load_(C1, SFO, P2)",
           "Load_(C2, JFK, P1)","Load_(C2, JFK, P2)","Load_(C2, SFO, P1)","Load_(C2, SFO, P2)",
           "Unload_(C1, JFK, P1)","Unload_(C1, JFK, P2)","Unload_(C1, SFO, P1)","Unload_(C1, SFO, P2)",
           "Unload_(C2, JFK, P1)","Unload_(C2, JFK, P2)","Unload_(C2, SFO, P1)","Unload_(C2, SFO, P2)",
           "Fly_(P1, JFK, SFO)","Fly_(P1, SFO, JFK)","Fly_(P2, JFK, SFO)","Fly_(P2, SFO, JFK)"]



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





#goal
# KB.tell(logic.expr("Fly_0(P1, SFO, JFK)"))
KB.tell(logic.expr("At_6(P1, JFK) & At_6(C1, JFK)"))
KB.tell(logic.expr("At_6(C2, SFO) & At_6(P2, SFO)"))


#some manual cnf
string = ""
for elem in KB.clauses:
#     print(elem)
#     elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


action_stubs = ["Load", "Unload", "Fly"]



#print only true values
answer = logic.dpll_satisfiable(logic.expr(string))


#print out only true actions, leave out facts
if answer != False: 
    for elem in answer:
        if answer[elem]:
            if any(sub in str(elem) for sub in action_stubs):
                print(str(elem)+ " : " +str(answer[elem]))
else:
    print(answer)
# print(logic.dpll_satisfiable(logic.expr(string)))
