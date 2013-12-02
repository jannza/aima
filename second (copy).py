import logic


KB = logic.PropKB()

#initial state
KB.tell(logic.expr("At_0(Flat, Axle) & At_0(Spare, Trunk)"))

#first
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_0(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | At_0(Flat, Ground)"))




#second
KB.tell(logic.expr("~Remove_0(Flat, Axle) | At_1(Flat, Ground)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | At_1(Flat, Axle)"))



#third
KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~At_1(Flat, Axle)"))
KB.tell(logic.expr("~PutOn_0(Flat, Axle) | ~At_1(Flat, Ground)"))




#fourth
KB.tell(logic.expr("At_0(Flat, Axle) | ~At_1(Flat, Axle) | PutOn_0(Flat, Axle)"))
KB.tell(logic.expr("At_0(Flat, Ground) | ~At_1(Flat, Ground) | Remove_0(Flat, Axle)"))



#fifth
KB.tell(logic.expr("~At_0(Flat, Axle) | At_1(Flat, Axle) | Remove_0(Flat, Axle)"))
KB.tell(logic.expr("~At_0(Flat, Ground) | At_1(Flat, Ground) | PutOn_0(Flat, Axle)"))



#sixth
KB.tell(logic.expr("~Remove_0(Flat, Axle) | ~PutOn_0(Flat, Axle)"))



#seventh
KB.tell(logic.expr("Remove_0(Flat, Axle) | PutOn_0(Flat, Axle)"))



#add goal
KB.tell(logic.expr("At_1(Flat, Ground)"))



#some manual cnf
string = ""
for elem in KB.clauses:
    elem = logic.to_cnf(str(elem))
    string = string + str(elem) + " & "
    
string = string[:-2]    


# print(string)


# answer = logic.dpll_satisfiable(string)
# 
# print(type(answer))

print(logic.dpll_satisfiable(string))


# print(logic.dpll_satisfiable("P&~P"))