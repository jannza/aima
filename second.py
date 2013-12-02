import logic
import itertools


KB = logic.PropKB()

#initial state

KB.tell(logic.expr("At_0(Flat, Axle) & ~At_0(Flat, Ground) & ~At_0(Flat, Trunk)"))
KB.tell(logic.expr("~At_0(Spare, Axle) & ~At_0(Spare, Ground) & At_0(Spare, Trunk)"))


# KB.tell(logic.expr("At_0(Flat, Axle) & At_0(Spare, Trunk)"))
# #initial locations imply parts are not elsewhere at the same time
# KB.tell(logic.expr("~At_0(Flat, Axle) | (~At_0(Flat, Trunk) & ~At_0(Flat, Ground))"))


#first
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_0(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | At_0(Flat, Ground) "))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | ~At_0(Flat, Axle) "))
KB.tell(logic.expr("~Remove_0(Flat, Trunk) | At_0(Flat, Trunk)"))


#second
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_1(Flat, Ground)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | At_1(Flat, Axle)"))
KB.tell(logic.expr("~Remove_0(Flat, Trunk) | At_1(Flat, Ground)"))



#third
KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | ~At_1(Flat, Ground)"))
KB.tell(logic.expr("~Remove_0(Flat, Trunk) | ~At_1(Flat, Trunk)"))


#fourth
KB.tell(logic.expr("At_0(Flat, Axle) | ~At_1(Flat, Axle) | PutOn_0(Flat, Axle)"))
KB.tell(logic.expr("At_0(Flat, Ground) | ~At_1(Flat, Ground) | Remove_0(Flat, Axle) | Remove_0(Flat, Trunk)"))
KB.tell(logic.expr("At_0(Flat, Trunk) | ~At_1(Flat, Trunk)"))



#fifth
KB.tell(logic.expr("~At_0(Flat, Axle) | At_1(Flat, Axle) | Remove_0(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Ground) | At_1(Flat, Ground) | PutOn_0(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Trunk) | At_1(Flat, Trunk) | Remove_0(Flat, Trunk)"))


#list of all possible actions
actions = ["Remove_0(Flat, Axle)", "PutOn_0(Flat, Axle)", "Remove_0(Flat, Trunk)"]

#sixth, this can somewhat be automated

for elem in itertools.combinations(actions, 2):
    KB.tell(logic.expr("~"+elem[0]+" | ~"+elem[1]))





# KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~PutOn_0(Flat, Axle)"))
# KB.tell(logic.expr("~PutOn_0(Flat, Axle) | ~Remove_0(Flat, Axle)"))


#seventh, can be also automated
seventh = ""
for elem in actions:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
 
KB.tell(logic.expr(seventh))



#add goal
KB.tell(logic.expr("At_1(Flat, Ground)"))



#some manual cnf
string = ""
for elem in KB.clauses:
#     print(elem)
    elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)


#print only true values
answer = logic.dpll_satisfiable(string)
if answer != False: 
    for elem in answer:
        if answer[elem]:
            print(str(elem)+ " : " +str(answer[elem]))
else:
    print(answer)
# print(logic.dpll_satisfiable(string))



