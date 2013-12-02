import logic


KB = logic.PropKB()

#initial state
KB.tell(logic.expr("At_0(Flat, Axle) & At_0(Spare, Trunk)"))
#initial locations imply parts are not elsewhere at the same time
KB.tell(logic.expr("~At_0(Spare, Trunk) | (~At_0(Spare, Axle) & ~At_0(Spare, Ground))"))



#first
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | At_0(Spare, Trunk)"))
KB.tell(logic.expr("~PutOn_0(Spare, Axle) | At_0(Spare, Ground)"))
KB.tell(logic.expr("~PutOn_0(Spare, Axle) | ~At_0(Flat, Axle) "))
KB.tell(logic.expr("~Remove_0(Spare, Axle) | At_0(Spare, Axle)"))


#second
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | At_1(Spare, Ground)"))
KB.tell(logic.expr("~PutOn_0(Spare, Axle) | At_1(Spare, Axle)"))
KB.tell(logic.expr("~Remove_0(Spare, Axle) | At_1(Spare, Ground)"))


#third
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("~PutOn_0(Spare, Axle) | ~At_1(Spare, Ground)"))
KB.tell(logic.expr("~Remove_0(Spare, Axle) | ~At_1(Spare, Axle)"))


#fourth
# KB.tell(logic.expr("At_0(Flat, Axle) | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("At_0(Spare, Ground) | ~At_1(Spare, Ground) | Remove_0(Spare, Trunk) | Remove_0(Spare, Axle)"))
KB.tell(logic.expr("At_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("At_0(Spare, Axle) | ~At_1(Spare, Axle) | PutOn_0(Spare, Axle)"))


#fifth
# KB.tell(logic.expr("~At_0(Flat, Axle) | At_1(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Spare, Ground) | At_1(Spare, Ground) | PutOn_0(Spare, Axle)"))
KB.tell(logic.expr("~At_0(Spare, Trunk) | At_1(Spare, Trunk) | Remove_0(Spare, Trunk)"))
KB.tell(logic.expr("~At_0(Spare, Axle) | At_1(Spare, Axle) | Remove_0(Spare, Axle)"))



#list of all possible actions
actions = ["Remove_0(Spare, Trunk)", "PutOn_0(Spare, Axle)", "Remove_0(Spare, Axle)"]


#sixth, this can somewhat be automated

for elem in actions:
    for elem2 in actions:
        if elem != elem2:
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))


#seventh, can be also automated
seventh = ""
for elem in actions:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
 
KB.tell(logic.expr(seventh))


#add goal
KB.tell(logic.expr("At_1(Spare, Ground)"))



#some manual cnf
string = ""
for elem in KB.clauses:
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

# print(logic.dpll_satisfiable(string))


