import logic
import itertools

KB = logic.PropKB()

#initial state
KB.tell(logic.expr("~At_0(Spare, Ground)"))
KB.tell(logic.expr("At_0(Spare, Trunk)"))
KB.tell(logic.expr("~At_0(Spare, Axle)"))
KB.tell(logic.expr("At_0(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Ground)"))
KB.tell(logic.expr("~At_0(Flat, Trunk)"))
KB.tell(logic.expr("~At_0(Flat, Trunk)"))





# KB.tell(logic.expr("At_1(Spare, Ground)"))
# KB.tell(logic.expr("At_1(Spare, Trunk)"))
# KB.tell(logic.expr("At_1(Spare, Axle)"))
# KB.tell(logic.expr("At_1(Flat, Axle)"))
# KB.tell(logic.expr("At_1(Flat, Ground)"))
# KB.tell(logic.expr("At_1(Flat, Trunk)"))
# KB.tell(logic.expr("At_1(Flat, Trunk)"))


##do not include not possible actions, will keep model simpler

#first
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | At_0(Spare, Trunk)"))
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_0(Flat, Axle)"))


#second
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | At_1(Spare, Ground)"))
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_1(Flat, Ground)"))



#third
KB.tell(logic.expr("~Remove_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~At_1(Flat, Axle)"))





#fourth
KB.tell(logic.expr("At_0(Spare, Ground) | ~At_1(Spare, Ground) | Remove_0(Spare, Trunk)"))
KB.tell(logic.expr("At_0(Spare, Trunk) | ~At_1(Spare, Trunk)"))
KB.tell(logic.expr("At_0(Spare, Axle) | ~At_1(Spare, Axle)"))
KB.tell(logic.expr("At_0(Flat, Axle) | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("At_0(Flat, Ground) | ~At_1(Flat, Ground) | Remove_0(Flat, Axle)"))
KB.tell(logic.expr("At_0(Flat, Trunk) | ~At_1(Flat, Trunk)"))



#fifth
KB.tell(logic.expr("~At_0(Spare, Ground) | At_1(Spare, Ground)"))
KB.tell(logic.expr("~At_0(Spare, Trunk) | At_1(Spare, Trunk) | Remove_0(Spare, Trunk)"))
KB.tell(logic.expr("~At_0(Spare, Axle) | At_1(Spare, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Axle) | At_1(Flat, Axle) | Remove_0(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Ground) | At_1(Flat, Ground)"))
KB.tell(logic.expr("~At_0(Flat, Trunk) | At_1(Flat, Trunk)"))


#list of all possible actions
actions = ["Remove_0(Spare, Trunk)", "Remove_0(Flat, Axle)"]



#sixth, this can somewhat be automated

for elem in actions:
    for elem2 in actions:
        if elem != elem2:
#             print(logic.expr("~"+elem+" | ~"+elem2))
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))


# for elem in itertools.combinations(actions, 2):
#     KB.tell(logic.expr("~"+elem[0]+" | ~"+elem[1]))



#seventh, can be also automated
seventh = ""
for elem in actions:    
    seventh = seventh + elem + " | "
seventh = seventh[:-2]
  
KB.tell(logic.expr(seventh))



#add goal
# KB.tell(logic.expr("At_1(Spare, Ground)"))


KB.tell(logic.expr("Remove_0(Spare, Trunk)"))
KB.tell(logic.expr("Remove_0(Flat, Axle)"))



#some manual cnf
string = ""
for elem in KB.clauses:
#     elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)

#print only true values
# answer = logic.dpll_satisfiable(string)
# if answer != False: 
#     for elem in answer:
# #         if answer[elem]:
#         print(str(elem)+ " : " +str(answer[elem]))
# else:
#     print(answer)
print(logic.dpll_satisfiable(string))
# print(logic.dpll_satisfiable("A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) & (B | ~C | D) & (A | ~E | F) & (~A | E | D)"))

# print(logic.dpll_satisfiable("A&~B"))

