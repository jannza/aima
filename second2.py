import logic
import itertools

KB = logic.PropKB()

#initial state

# KB.tell(logic.expr("~At0SpareGround | At_0(Spare,Trunk) | ~At_0(Spare,Axle)"))
# 
# 
# KB.tell(logic.expr("At_0(Flat,Axle) | ~At_0(Flat,Ground) | ~At_0(Flat,Trunk)"))


KB.tell(logic.expr("~At0SpareGround"))
KB.tell(logic.expr("At_0(Spare,Trunk)"))
KB.tell(logic.expr("~At_0(Spare,Axle)"))
KB.tell(logic.expr("At_0(Flat,Axle)"))
KB.tell(logic.expr("~At_0(Flat,Ground)"))
KB.tell(logic.expr("~At_0(Flat,Trunk)"))


##do not include not possible actions,will keep model simpler

#first
KB.tell(logic.expr("~Remove0SpareTrunk | At_0(Spare,Trunk)"))
KB.tell(logic.expr("~Remove_0(Flat,Axle) | At_0(Flat,Axle)"))

KB.tell(logic.expr("~Remove_1(Spare,Trunk) | At_1(Spare,Trunk)"))
KB.tell(logic.expr("~Remove_1(Flat,Axle) | At_1(Flat,Axle)"))


#second
KB.tell(logic.expr("~Remove0SpareTrunk | At_1(Spare,Ground)"))
KB.tell(logic.expr("~Remove_0(Flat,Axle) | At_1(Flat,Ground)"))

KB.tell(logic.expr("~Remove_1(Spare,Trunk) | At_2(Spare,Ground)"))
KB.tell(logic.expr("~Remove_1(Flat,Axle) | At_2(Flat,Ground)"))

#third
KB.tell(logic.expr("~Remove0SpareTrunk | ~At_1(Spare,Trunk)"))
KB.tell(logic.expr("~Remove_0(Flat,Axle) | ~At_1(Flat,Axle)"))

KB.tell(logic.expr("~Remove_1(Spare,Trunk) | ~At_2(Spare,Trunk)"))
KB.tell(logic.expr("~Remove_1(Flat,Axle) | ~At_2(Flat,Axle)"))




#fourth from false to true
KB.tell(logic.expr("At0SpareGround | ~At_1(Spare,Ground) | Remove0SpareTrunk"))
# KB.tell(logic.expr("At_0(Spare,Trunk) | ~At_1(Spare,Trunk)"))
# KB.tell(logic.expr("At_0(Spare,Axle) | ~At_1(Spare,Axle)"))
# KB.tell(logic.expr("At_0(Flat,Axle) | ~At_1(Flat,Axle)"))
KB.tell(logic.expr("At_0(Flat,Ground) | ~At_1(Flat,Ground) | Remove_0(Flat,Axle)"))
# KB.tell(logic.expr("At_0(Flat,Trunk) | ~At_1(Flat,Trunk)"))


KB.tell(logic.expr("At_1(Spare,Ground) | ~At_2(Spare,Ground) | Remove_1(Spare,Trunk)"))
# KB.tell(logic.expr("At_1(Spare,Trunk) | ~At_2(Spare,Trunk)"))
# KB.tell(logic.expr("At_1(Spare,Axle) | ~At_2(Spare,Axle)"))
# KB.tell(logic.expr("At_1(Flat,Axle) | ~At_2(Flat,Axle)"))
KB.tell(logic.expr("At_1(Flat,Ground) | ~At_2(Flat,Ground) | Remove_1(Flat,Axle)"))
# KB.tell(logic.expr("At_1(Flat,Trunk) | ~At_2(Flat,Trunk)"))



#fifth from true to false
# KB.tell(logic.expr("~At0SpareGround | At_1(Spare,Ground)"))
KB.tell(logic.expr("~At_0(Spare,Trunk) | At_1(Spare,Trunk) | Remove0SpareTrunk"))
# KB.tell(logic.expr("~At_0(Spare,Axle) | At_1(Spare,Axle)"))
KB.tell(logic.expr("~At_0(Flat,Axle) | At_1(Flat,Axle) | Remove_0(Flat,Axle)"))
# KB.tell(logic.expr("~At_0(Flat,Ground) | At_1(Flat,Ground)"))
# KB.tell(logic.expr("~At_0(Flat,Trunk) | At_1(Flat,Trunk)"))


# KB.tell(logic.expr("~At_1(Spare,Ground) | At_2(Spare,Ground)"))
KB.tell(logic.expr("~At_1(Spare,Trunk) | At_2(Spare,Trunk) | Remove_1(Spare,Trunk)"))
# KB.tell(logic.expr("~At_1(Spare,Axle) | At_2(Spare,Axle)"))
KB.tell(logic.expr("~At_1(Flat,Axle) | At_2(Flat,Axle) | Remove_1(Flat,Axle)"))
# KB.tell(logic.expr("~At_1(Flat,Ground) | At_2(Flat,Ground)"))
# KB.tell(logic.expr("~At_1(Flat,Trunk) | At_2(Flat,Trunk)"))

#list of all possible actions
actions = ["Remove0SpareTrunk","Remove_0(Flat,Axle)"]



actions2 = ["Remove_1(Spare,Trunk)","Remove_1(Flat,Axle)"]

#sixth,this can somewhat be automated

for elem in actions:
    for elem2 in actions:
        if elem != elem2:
            print(logic.expr("~"+elem+" | ~"+elem2))
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))
             
             
             
for elem in actions2:
    for elem2 in actions2:
        if elem != elem2:
            print(logic.expr("~"+elem+" | ~"+elem2))
            KB.tell(logic.expr("~"+elem+" | ~"+elem2))


# for elem in itertools.combinations(actions,2):
# #     print(logic.expr("~"+elem[0]+" | ~"+elem[1]))
#     KB.tell(logic.expr("~"+elem[0]+" | ~"+elem[1]))
# 
# 
# for elem in itertools.combinations(actions2,2):
#     KB.tell(logic.expr("~"+elem[0]+" | ~"+elem[1]))


#seventh,can be also automated
seventh = ""

KB.tell(logic.expr("Remove0SpareTrunk | Remove_0(Flat,Axle)"))
# for elem in actions:    
#     seventh = seventh + elem + " | "
# seventh = seventh[:-2]
# print(logic.expr(seventh))  
# 
# KB.tell(logic.expr(seventh))
 
 
seventh = ""

KB.tell(logic.expr("Remove_1(Spare,Trunk) | Remove_1(Flat,Axle)"))

# for elem in actions2:    
#     seventh = seventh + elem + " | "
# seventh = seventh[:-2]
# print(logic.expr(seventh))  
# KB.tell(logic.expr(seventh))

#add goal

# KB.tell(logic.expr("Remove_0(Flat,Axle) & Remove_1(Spare,Trunk)"))


# KB.tell(logic.expr("Remove0SpareTrunk"))
# KB.tell(logic.expr("Remove_0(Flat,Axle)"))


# KB.tell(logic.expr("At_2(Flat,Ground) & At_2(Spare,Ground)"))




KB.tell(logic.expr("At_2(Flat,Ground)"))   
KB.tell(logic.expr("At_2(Spare,Ground)"))



#some manual cnf
string = ""
for elem in KB.clauses:
    elem = logic.to_cnf(str(elem))
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


