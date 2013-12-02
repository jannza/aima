import logic
import itertools

KB = logic.PropKB()



#Initial
KB.tell(logic.expr("On_0(cap, flash)"))
KB.tell(logic.expr("~In_0(battery1, flash)"))
KB.tell(logic.expr("~In_0(battery2, flash)"))


#goal
KB.tell(logic.expr("On_4(cap, flash)"))
KB.tell(logic.expr("In_4(battery1, flash)"))
KB.tell(logic.expr("In_4(battery2, flash)"))


#some more
for elem in range(0,4):
    KB.tell(logic.expr("~Place_"+str(elem)+" | (~On_"+str(elem)+"(cap, flash) & On_"+str(elem+1)+"(cap, flash))"))
    KB.tell(logic.expr("Remove_"+str(elem)+" | (On_"+str(elem)+"(cap, flash) & ~On_"+str(elem+1)+"(cap, flash))"))
    KB.tell(logic.expr("~Insert1_"+str(elem)+" | (~On_"+str(elem)+"(cap, flash) & ~In_"+str(elem)+"(battery1, flash) & In_"+str(elem+1)+"(battery1, flash))"))
    KB.tell(logic.expr("~Insert2_"+str(elem)+" | (~On_"+str(elem)+"(cap, flash) & ~In_"+str(elem)+"(battery2, flash) & In_"+str(elem+1)+"(battery2, flash))"))

    

#frame axioms

for elem in range(0,4):
    KB.tell(logic.expr("(On_"+str(elem)+"(cap, flash) | ~On_"+str(elem+1)+"(cap, flash)) | Place_"+str(elem)))
    KB.tell(logic.expr("(~On_"+str(elem)+"(cap, flash) | On_"+str(elem+1)+"(cap, flash)) | Remove_"+str(elem)))
    KB.tell(logic.expr("(In_"+str(elem)+"(battery1, flash) | ~In_"+str(elem+1)+"(battery1, flash)) | Insert1"+str(elem)))
    KB.tell(logic.expr("(~In_"+str(elem)+"(battery1, flash) | In_"+str(elem+1)+"(battery1, flash))"))
    KB.tell(logic.expr("(In_"+str(elem)+"(battery2, flash) | ~In_"+str(elem+1)+"(battery2, flash)) | Insert2"+str(elem)))
    KB.tell(logic.expr("(~In_"+str(elem)+"(battery2, flash) | In_"+str(elem+1)+"(battery2, flash))"))





#complete exclusiOn axioms
for elem in range(0,4):
    KB.tell(logic.expr("~Remove_"+str(elem)+" | ~Place_"+str(elem)))
    KB.tell(logic.expr("~Place_"+str(elem)+" | ~Insert1_"+str(elem)))
    KB.tell(logic.expr("~Remove_"+str(elem)+" | ~Insert1_"+str(elem)))
    KB.tell(logic.expr("~Place_"+str(elem)+" | ~Insert2_"+str(elem)))
    KB.tell(logic.expr("~Remove_"+str(elem)+" | ~Insert2_"+str(elem)))
    KB.tell(logic.expr("~Insert1_"+str(elem)+" | ~Insert2_"+str(elem)))



#some manual cnf
string = ""
for elem in KB.clauses:
#     elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# prInt(strIng)

#prInt Only true values
# answer = logic.dpll_satisfiable(strIng)
# if answer != False: 
#     for elem In answer:
# #         if answer[elem]:
#         prInt(str(elem)+ " : " +str(answer[elem]))
# else:
#     prInt(answer)
print(logic.dpll_satisfiable(string))
# prInt(logic.dpll_satisfiable("A & ~B & C & (A | ~D) & (~E | ~D) & (C | ~D) & (~A | ~F) & (E | ~F) & (~D | ~F) & (B | ~C | D) & (A | ~E | F) & (~A | E | D)"))

# prInt(logic.dpll_satisfiable("A&~B"))

