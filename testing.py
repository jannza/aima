import logic
import itertools

KB = logic.PropKB()



#Initial
KB.tell(logic.expr("On1(cap, flash)"))
KB.tell(logic.expr("~In1(battery1, flash)"))
KB.tell(logic.expr("~In1(battery2, flash)"))


#goal
KB.tell(logic.expr("On5(cap, flash)"))
KB.tell(logic.expr("In5(battery1, flash)"))
KB.tell(logic.expr("In5(battery2, flash)"))


#some more
for elem in range(1,5):
    KB.tell(logic.expr("~Place"+str(elem)+" | (~On"+str(elem)+"(cap, flash) & On"+str(elem+1)+"(cap, flash))"))
    KB.tell(logic.expr("~Remove"+str(elem)+" | (On"+str(elem)+"(cap, flash) & ~On"+str(elem+1)+"(cap, flash))"))
    KB.tell(logic.expr("~Insert1"+str(elem)+" | (~On"+str(elem)+"(cap, flash) & ~In"+str(elem)+"(battery1, flash) & In"+str(elem+1)+"(battery1, flash))"))
    KB.tell(logic.expr("~Insert2"+str(elem)+" | (~On"+str(elem)+"(cap, flash) & ~In"+str(elem)+"(battery2, flash) & In"+str(elem+1)+"(battery2, flash))"))

    

#frame axioms

for elem in range(1,5):
    KB.tell(logic.expr("(On"+str(elem)+"(cap, flash) | ~On"+str(elem+1)+"(cap, flash)) | Place"+str(elem)))
    KB.tell(logic.expr("(~On"+str(elem)+"(cap, flash) | On"+str(elem+1)+"(cap, flash)) | Remove"+str(elem)))
    KB.tell(logic.expr("(In"+str(elem)+"(battery1, flash) | ~In"+str(elem+1)+"(battery1, flash)) | Insert1"+str(elem)))
    KB.tell(logic.expr("(~In"+str(elem)+"(battery1, flash) | In"+str(elem+1)+"(battery1, flash))"))
    KB.tell(logic.expr("(In"+str(elem)+"(battery2, flash) | ~In"+str(elem+1)+"(battery2, flash)) | Insert2"+str(elem)))
    KB.tell(logic.expr("(~In"+str(elem)+"(battery2, flash) | In"+str(elem+1)+"(battery2, flash))"))





#complete exclusiOn axioms
for elem in range(1,5):
    KB.tell(logic.expr("~Remove"+str(elem)+" | ~Place"+str(elem)))
    KB.tell(logic.expr("~Place"+str(elem)+" | ~Insert1"+str(elem)))
    KB.tell(logic.expr("~Remove"+str(elem)+" | ~Insert1"+str(elem)))
    KB.tell(logic.expr("~Place"+str(elem)+" | ~Insert2"+str(elem)))
    KB.tell(logic.expr("~Remove"+str(elem)+" | ~Insert2"+str(elem)))
    KB.tell(logic.expr("~Insert1"+str(elem)+" | ~Insert2"+str(elem)))



#some manual cnf
string = ""
for elem in KB.clauses:
#     elem = logic.tocnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)
# print(logic.to_cnf(string))

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


